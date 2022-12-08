FROM confluentinc/cp-kafka-connect:6.1.0

LABEL maintainer="Naren Ravilla"

ARG DBZ_CONNECTOR_POSTGRES=1.4.2

ENV DBZ_CONNECTOR_POSTGRES=${DBZ_CONNECTOR_POSTGRES}

USER root

RUN wget "https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/${DBZ_CONNECTOR_POSTGRES}.Final/debezium-connector-postgres-${DBZ_CONNECTOR_POSTGRES}.Final-plugin.tar.gz" && \
tar xfz $PWD/debezium-connector-postgres-${DBZ_CONNECTOR_POSTGRES}.Final-plugin.tar.gz -C $PWD && \
cp $PWD/debezium-connector-postgres/*.jar /usr/share/java/kafka/