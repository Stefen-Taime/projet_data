# import libraries
import os
import pandas as pd
from dotenv import load_dotenv
from request import Requests
from datetime import datetime
from minio import Minio
from io import BytesIO

# get env
load_dotenv()

# load variables
size = os.getenv("SIZE")
minio = os.getenv("MINIO")
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
landing = os.getenv("LANDING_BUCKET")


# set up parameters to request from api call
params = {'size': size}


# class to insert into datastore
class MinioStorage(object):

    @staticmethod
    def write_movies_json():
        
        # file name + datetime
        # example = manufacturers_2022_11_29_14_47_22.json
        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        hour = datetime.today().hour
        minute = datetime.today().minute
        second = datetime.today().second
        
        stable_datasets = os.getenv("DATA")

        datasets_df = pd.read_csv(stable_datasets, sep=',')
        
        # convert python list (dict)
        # use pandas dataframe to ease the insert of the data
        pd_df_data = pd.DataFrame.from_dict(datasets_df)
       
        # add [dt_current_timestamp] into dataframe
        pd_df_data['dt_current_timestamp'] = Requests().gen_timestamp()
       

        # connect into minio
        # providing access and key
        # share connection among the function(s)
        client = Minio(minio, access_key, secret_key, secure=False)

        # movies
        entity =  os.getenv("BUCKET")
        name = entity + f'/{entity}_{year}_{month}_{day}_{hour}_{minute}_{second}.json'
        json_data = pd_df_data.to_json(orient="records").encode('utf-8')
        json_buffer = BytesIO(json_data)
        client.put_object(landing, name, data=json_buffer, length=len(json_data), content_type='application/json')
        print(name)

      
    @staticmethod
    def write_into_landing_zone_json(entity):
        # set correct file name
        # file name + datetime
        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        hour = datetime.today().hour
        minute = datetime.today().minute
        second = datetime.today().second
        file_name = entity + f'/{entity}_{year}_{month}_{day}_{hour}_{minute}_{second}.json'