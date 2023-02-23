# Databricks notebook source
# MAGIC %python
# MAGIC # This is the main way to create a dataframe, using spark.read
# MAGIC path="dbfs:/mnt/athena-prod-1-nonpii/warehouse/edw/common_member_activity/"
# MAGIC commonActivity=spark.read.format("delta").load(path)
# MAGIC commonActivity.createOrReplaceTempView("common_member_activity")
# MAGIC display(commonActivity)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step one: Create a Schema to organize your tables

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists foobar

# COMMAND ----------

# MAGIC %md
# MAGIC ## First method (not preferred) - Copy data with CTAS

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This creates a full point-in-time copy.  Not the best but OK if for example you're joining two tables together and want to save the resulting table.
# MAGIC -- To refresh
# MAGIC create or replace table foobar.cma as select * from common_member_activity limit 100

# COMMAND ----------

# MAGIC %md
# MAGIC ## Second Method (Preferred) - Create a reference to data on disk with LOCATION keyword

# COMMAND ----------

# MAGIC %sql
# MAGIC create table foobar.cma_remote location "dbfs:/mnt/athena-prod-1-nonpii/warehouse/edw/common_member_activity/"

# COMMAND ----------

# MAGIC %md
# MAGIC ## HOT TIP: Use describe table extended to see the path to tables you already have in the Data tab

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table extended athena_health_survey.fact_survey_event
# MAGIC -- Look at the "Location" element to see the path to this table.  You can grab other paths to other tables once you know the base path

# COMMAND ----------

# MAGIC %md
# MAGIC Location = dbfs:/mnt/athena-prod-1-nonpii/warehouse/edw/fact_survey_event.  
# MAGIC Can do same in Azure.  Use this to poke your way around the different buckets.  Once you have a bucket you're able to use LS to dig deeper
