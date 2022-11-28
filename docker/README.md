## Docker Stacks

```shell

# deploy relational database for mysql and postgres && adminer client stack
docker-compose -f docker-compose-sql.yml up -d

# deploy minio stack on port 9000
docker-compose -f docker-compose-s3.yml up -d
```