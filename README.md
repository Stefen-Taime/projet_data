## End to end data engineering project with Spark, Mongodb, Minio, postgres and Metabase
### Utilizing of open source technologies for the implementation of a data pipeline
## Architecture

![End to end data enginering pipeline](https://github.com/Stefen-Taime/projet_data/blob/main/images/archi.png)
## Source Code
All the source code demonstrated in this post is open-source and available on [GitHub](https://github.com/Stefen-Taime/projet_data).
git clone https://github.com/Stefen-Taime/projet_data.git
## Prerequisites
As a prerequisite for this post, you will need to create the following resources:
1. (1) Linux Machine;
2. (1) Docker ;
3. (1) Docker Compose;
4. (1) Virtualenv;
### Setup
git clone https://github.com/Stefen-Taime/projet_data.git
cd projet_data/extractor

pip install -r requirements.txt
python main.py

or

docker build --tag=extractor .
docker-compose up run

#This folder contains code used to create a downlaods folder, iteratively download files from a list of uris, unzip them and delete zip files.
At this point you should have in the extractor directory with a new folder Dowloads with 2 csv files
### then
cd ..
cd docker

docker-compose -f docker-compose-nosql.yml up -d  #for mongodb
docker-compose -f docker-compose-sql.yml up -d    #for postgres and adminer port 8085, metabase port 3000
docker-compose -f docker-compose-s3.yml up -d     #for minio port 9000
docker-compose -f docker-compose-spark.yml up -d  #for spark master and jupyter notebook port 8888

cd ..
cd loader
pip install -r requirements.txt

# ! modify the path DATA and DATA_FOR_MONGODB variables in .env

python loader.py mongodb  #upload data in mongodb database (if you have an error, manually create an auto-mpg database and enter an auto collection and try again)
python loader.py minio    #upload data in minio(if you have an error, manually create a landing compartment and try again)
He must have now an auto-mpg database and inside an auto collection with data in it for mongodb and also data in minio
![mongodb compass](https://github.com/Stefen-Taime/projet_data/blob/main/images/mongodb.png)
![Minio](https://github.com/Stefen-Taime/projet_data/blob/main/images/minio.png)
### then
go to localhost 8888 and the password is "stefen".once in jupyter notebook run all cells
go to localhost 8085
![Minio](https://github.com/Stefen-Taime/projet_data/blob/main/images/adminer.png)
go to localhost 3000
![Minio](https://github.com/Stefen-Taime/projet_data/blob/main/images/dashboard.png)
## Cleaning Up