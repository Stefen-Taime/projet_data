# import libraries
import numpy as np
import requests
from datetime import datetime
from requests.exceptions import HTTPError

class Requests(object):

    # current timestamp
    # set date and time
    @staticmethod
    def gen_timestamp():
        return datetime.now()
        # call request with parameters
        # amount of rows to be requested

      