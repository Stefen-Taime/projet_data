# import libraries
import os
import sys
import argparse
import warnings
from dotenv import load_dotenv
from s3.minio_load import MinioStorage
from mongo.mongodb_load import MongoDB
from mysql.Mysql_load import MySQL

# warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# get env
load_dotenv()

# main
if __name__ == '__main__':

    # instantiate arg parse
    parser = argparse.ArgumentParser(description='python application for ingesting data')

    # add parameters to arg parse
    parser.add_argument('entity', type=str, choices=[
        'minio',
        'mysql',
        'mongodb',
    ], help='entities')

    # invoke help if null
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if sys.argv[1] == 'minio':
        MinioStorage().write_movies_json()
        
    if sys.argv[1] == 'mysql':
        MySQL().insert_rows()    
             
    # nosql databases
    if sys.argv[1] == 'mongodb':
        MongoDB().insert_rows()        