## Docker Stacks

```shell

# deploy sql stack
docker-compose -f docker-compose-sql.yml up -d

# deploy minio stack on port 9000
docker-compose -f docker-compose-s3.yml up -d
```