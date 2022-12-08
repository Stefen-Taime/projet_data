FROM --platform=linux/arm debezium/postgres:13

LABEL maintainer="Naren Ravilla"

COPY postgresql.conf.sample /usr/share/postgresql/postgresql.conf

COPY start-up.sql /docker-entrypoint-initdb.d
