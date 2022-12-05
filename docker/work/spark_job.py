import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from delta import *
print(pyspark.__version__)

conf = pyspark.SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.12:3.0.1").setMaster("local").setAppName("Spark-Job").setAll([('spark.driver.memory', '1g'),('spark.executor.memory','1g')])
sc = SparkContext(conf=conf)
sqlC = SQLContext(sc)

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
spark._jsc.hadoopConfiguration().set("spark.mongodb.input.uri", "mongodb://mongodb/auto-mpg.auto")
spark._jsc.hadoopConfiguration().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.10-2.2.10")


df_business = spark.read \
        .format("json") \
        .option("inferSchema", "true") \
        .json("s3a://landing/manufacturers//*.json")

df_business.show()
mongo_ip = "mongodb://mongodb:27017/auto-mpg."
print(mongo_ip)

iris = sqlC.read.format('com.mongodb.spark.sql.DefaultSource').option("uri", mongo_ip + "auto").load()
iris.createOrReplaceTempView("auto")
iris= sqlC.sql("SELECT * FROM auto")
iris.show()