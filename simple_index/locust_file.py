
import random
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser
import json


log = logging.getLogger("rest-api-short-urls")

data = json.load(open('db_data.json', 'r'))["ids"]

class LocustClient(FastHttpUser):
    wait_time = constant(0)
    host = "http://localhost:8000/ids"


    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)


    @task
    def test_get_items(self):

        try:
            id_val = random.choice(data)
            with self.client.get(f'/{id_val}', name='get id value') as resp_of_api:
                if resp_of_api.status_code == 200:
                    log.info("API call resulted in success.")
                else:
                    log.error("API call resulted in failed.")
             
        except Exception as e:
            log.error(f"Exception occurred! details are {e}")