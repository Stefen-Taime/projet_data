# import libraries
import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

# get env
load_dotenv()

# load variables
mongodb = os.getenv("MONGODB_SERVER")
mongodb_database = os.getenv("MONGODB_DATABASE")
size = os.getenv("SIZE")

# class to insert into datastore
class MongoDB(object):

    @staticmethod
    def insert_rows():
        
        # convert python list (dict)
        # use pandas dataframe to ease the insert of the data
        
        stable_datasets = os.getenv("DATA_FOR_MongoDB")
        datasets_df = pd.read_csv(stable_datasets, sep=',')
        pd_df = pd.DataFrame.from_dict(datasets_df) 

        # connecting into mongodb
        # set database connectivity
        client = MongoClient(mongodb)
        db = client[mongodb_database]

        # setting up collection to insert data
        # pandas dataframe
        collection_auto = db['auto']
       
       
        # get records from dataframe
        # insert into collection
        pd_df.reset_index(inplace=True)
        data_dict = pd_df.to_dict("records")
        collection_auto.insert_many(data_dict)