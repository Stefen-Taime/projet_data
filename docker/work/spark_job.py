#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext


# In[3]:


print(pyspark.__version__)


# In[15]:


####### read from mongodb ########
url = 'mongodb://mongodb:27017/auto-mpg.auto'
spark = (SparkSession
         .builder
         .master('local[*]')
         .config('spark.driver.extraClassPath','path_to_jars/*')
         .config("spark.mongodb.read.connection.uri",url)
         .config("spark.mongodb.write.connection.uri", url)
         .getOrCreate()
         )
auto_df = spark.read.format("mongodb").load()
auto_df.createOrReplaceTempView("auto")
auto_df= spark.sql("SELECT _id, acceleration, carname, horsepower, cylinders, modelyear, mpg, origin FROM auto")
auto_df.show()


# In[22]:


import pyspark
from delta import *
import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("DeltaApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") 

spark = configure_spark_with_delta_pip(builder).master("spark://spark:7077").getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://minio:9000")
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "FFD34B2AC56E76E8BB9E7EFD7D283")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "47A13EFAB1CA1F253FD6F56DEF769")
spark._jsc.hadoopConfiguration().set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
spark._jsc.hadoopConfiguration().set("spark.jars", "postgresql-42.2.14.jar")


# In[14]:


# read from minio
df_manufacturers = spark.read \
        .format("json") \
        .option("inferSchema", "true") \
        .json("s3a://landing/manufacturers//*.json")

df_manufacturers.show()


# In[ ]:





# In[16]:


from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

#Join two DataFrames with an expression
# Add a manufacturers column, to join with the manufacturers list.
first_word_udf = udf(lambda x: x.split()[0], StringType())
df = auto_df.withColumn("manufacturer", first_word_udf(auto_df.carname))

# The actual join.
df_join = df.join(
    df_manufacturers,
    (df.manufacturer == df_manufacturers.manufacturer)
    | (df.mpg == df_manufacturers.manufacturer),
)
#drop column
df_final = df_join.drop("dt_current_timestamp")
colnames = df_final.columns
df_final = df_final.toDF(*map(str, range(len(colnames))))\
    .drop(str(len(colnames)-1))\
    .toDF(*colnames[:-1])
df_final.show()


# In[24]:


jdbcDF = spark.read.format("jdbc"). \
options(
         url='jdbc:postgresql://postgres:5432/postgres', # jdbc:postgresql://<host>:<port>/<database>
         dbtable='test',
         user='postgres',
         password='Sup3rS3c3t',
         driver='org.postgresql.Driver').\
load()


# In[26]:


df_final.write \
    .jdbc(
        url='jdbc:postgresql://postgres:5432/postgres', 
        table="public.auto", 
        properties={"user": "postgres", "password": "Sup3rS3c3t"}
    )
