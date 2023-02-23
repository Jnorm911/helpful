# Databricks notebook source
# MAGIC %md
# MAGIC ## Basic feature searches for documentation 🖋️

# COMMAND ----------

# MAGIC %md
# MAGIC Listing all tables of "User Facts"

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC path="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts"
# MAGIC display(dbutils.fs.ls(path))

# COMMAND ----------

# MAGIC %md
# MAGIC ##In-depth search examples 📖

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC path="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts/activity/"
# MAGIC dataframe=spark.read.format("parquet").load(path)
# MAGIC #for sql
# MAGIC dataframe.createOrReplaceTempView("activity")
# MAGIC #display(dataframe)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC describe table activity

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from activity
# MAGIC where client_activity_idt_event_count_12month > 0
# MAGIC limit 20

# COMMAND ----------

# MAGIC %md
# MAGIC ##Quick Table Search 🔎

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC path="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts/campaign/"
# MAGIC display(dbutils.fs.ls(path))

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC path="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts/membership/member_profile_information/"
# MAGIC df=spark.read.format("delta").load(path)
# MAGIC display(df)
# MAGIC df.createOrReplaceTempView("2sql")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC SQL refined search

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select *
# MAGIC from 2sql
# MAGIC where 
# MAGIC email_missions_join_digest_yes > 0
# MAGIC limit 20

# COMMAND ----------

# MAGIC %md 
# MAGIC **How to get index_dt** 
# MAGIC 
# MAGIC (step 1 for How to Page)

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC indexPath="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts/membership/member_profile_information/"
# MAGIC dbutils.fs.ls(indexPath)

# COMMAND ----------

# MAGIC %md
# MAGIC **Append index_dt to df**
# MAGIC 
# MAGIC (step 2 for How To Page)

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC path="dbfs:/mnt/athena-prod-1-pii/warehouse/edw/personalization_feature_store/user_facts/membership/member_profile_information/index_dt=2022-01-01"
# MAGIC df=spark.read.format("delta").load(path)
# MAGIC display(df)

# COMMAND ----------


