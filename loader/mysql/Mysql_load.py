# import libraries
import os
import pandas as pd
from dotenv import load_dotenv
from helper.request import Requests
from sqlalchemy import create_engine

# get env
load_dotenv()

# load variables
mysql = os.getenv("MYSQL")
size = os.getenv("SIZE")

# set up parameters to request from api call
params = {'size': size}

# class to insert into datastore
class MySQL(object):

    @staticmethod
    def insert_rows():
        # get request [api] to store in a variable
        # using method get to retrieve data
        stable_datasets = os.getenv("DATA")

        datasets_df = pd.read_csv(stable_datasets, sep=',')  

        # convert python list (dict)
        # use pandas dataframe to ease the insert of the data
        pd_df_auto = pd.DataFrame.from_dict(datasets_df)
        mysql_engine = create_engine(mysql)
        pd_df_auto.to_sql('auto', mysql_engine, if_exists='append', index=False, chunksize=100)
     


