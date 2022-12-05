FROM docker.io/bitnami/spark:3.2.1

COPY ./jars/ /opt/bitnami/spark/jars/

# USER root
# # needed so that thrift server can create the megastore_db directory
# RUN chmod g+w /opt/bitnami/spark

# USER 1001
# CMD ["/bin/bash", "-c","/opt/bitnami/spark/bin/spark-submit --class org.apache.spark.sql.hive.thriftserver.HiveThriftServer2"]
