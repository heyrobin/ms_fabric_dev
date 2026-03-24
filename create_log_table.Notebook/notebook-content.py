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
# META     },
# META     "warehouse": {
# META       "default_warehouse": "95c5fd4d-b591-a76f-4382-d3123a022c71",
# META       "known_warehouses": [
# META         {
# META           "id": "95c5fd4d-b591-a76f-4382-d3123a022c71",
# META           "type": "Datawarehouse"
# META         },
# META         {
# META           "id": "2477fd56-df66-44ed-8ee0-45fb5d397848",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *

schema = StructType([
    StructField("table_name", StringType(), True),
    StructField("load_date", StringType(), True),
    StructField("status", StringType(), True),
    StructField("rows_loaded", IntegerType(), True),
    StructField("error_message", StringType(), True),
    StructField("ingestion_time", TimestampType(), True)
])

df = spark.createDataFrame([], schema)

df.write.format("delta").saveAsTable("dbo.bronze_ingestion_log")

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
