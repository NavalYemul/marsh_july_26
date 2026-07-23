# Databricks notebook source
catalog=dbutils.widgets.get("catalog")

# COMMAND ----------

df=spark.read.table(f"{catalog}.bronze.sales")

# COMMAND ----------

df1=df.dropDuplicates().dropna().drop("file_path","file_name","ingestion_time")

# COMMAND ----------

df1.write.mode("overwrite").saveAsTable(f"{catalog}.silver.sales_cleaned")