# import libraries
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# get env
load_dotenv()

# load variables
# get from env
mysql = os.getenv("MYSQL")

# building engines for relational databases
# postgres, mysql and mssql
mysql_engine = create_engine(mysql)
"""
# mysql
create table owshq.auto
(
    manufacturer text null,
    country text null
);

"""