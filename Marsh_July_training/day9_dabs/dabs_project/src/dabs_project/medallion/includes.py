# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

def add_metadata_col(df):
    df1=df.withColumn("file_path", col("_metadata.file_path")) \
    .withColumn("file_name",col("_metadata.file_name")) \
    .withColumn("ingestion_time", current_timestamp())
    return df1