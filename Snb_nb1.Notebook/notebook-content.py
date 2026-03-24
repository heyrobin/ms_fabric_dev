# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "85f1ab87-694d-4363-b4ff-998c675eb702",
# META       "default_lakehouse_name": "LH_Bronze",
# META       "default_lakehouse_workspace_id": "478a9b9c-d8be-4250-94b4-c7fc778777b5",
# META       "known_lakehouses": [
# META         {
# META           "id": "85f1ab87-694d-4363-b4ff-998c675eb702"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = (
    spark.readStream
    .format("eventhubs")
    .options(**eventhub_config)
    .load()
)

df.writeStream \
    .format("parquet") \
    .option("path", "Files/bronze/source=eventhub/table=sales/") \
    .option("checkpointLocation", "Files/checkpoints/sales/") \
    .start()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.table("dbo.sales_raw")

df.write.mode("overwrite").saveAsTable("bronze.dim_store_raw")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
