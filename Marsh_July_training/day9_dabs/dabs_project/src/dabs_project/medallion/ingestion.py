# Databricks notebook source
# MAGIC %run "/Workspace/Users/naval.datamaster@gmail.com/marsh_july_26/dabs_project/src/dabs_project/medallion/includes"

# COMMAND ----------

#dbutils.widgets.text("catalog","default")
catalog=dbutils.widgets.get("catalog")

# COMMAND ----------

df=spark.read.csv(f"/Volumes/{catalog}/bronze/raw/",header=True,inferSchema=True)

df_with_metadata=add_metadata_col(df)

df_with_metadata.write.mode("overwrite").saveAsTable(f"{catalog}.bronze.sales")