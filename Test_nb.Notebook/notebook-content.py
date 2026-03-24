# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "85f1ab87-694d-4363-b4ff-998c675eb702",
# META       "default_lakehouse_name": "Bronze",
# META       "default_lakehouse_workspace_id": "478a9b9c-d8be-4250-94b4-c7fc778777b5",
# META       "known_lakehouses": [
# META         {
# META           "id": "85f1ab87-694d-4363-b4ff-998c675eb702"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************


# CELL ********************

df = spark.sql("SELECT * FROM Bronze.dbo.kl LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from Bronze.dbo.kl

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
