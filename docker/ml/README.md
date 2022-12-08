## Debezium Kafka Connect Setup
---
A single node setup of Postgresql, Debezium Postgres connector and kafka cluster.

* Simply use the command below to bring up the setup
```sh
$ docker-compose up --build -d
```

* After bringing up the infrastructure, we need to create a connector using API endpoint of kafka connect instance

```sh
$ curl --location --request POST 'http://localhost:8083/connectors' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "postgres-dbz-connector",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "dbzpostgres",
        "database.port": "5432",
        "database.user": "postgres",
        "database.password": "DebPostgres1!",
        "database.dbname" : "postgres",
        "table.include.list": "public.customers, public.orders",
        "topic.prefix": "dbz-",
        "tasks.max": "1",
        "database.server.name": "debezium-demo"
    }
}'
```

**Here is a reference architecture diagram**


![alt text](DBZ-Kafka_Connect.png?raw=true)