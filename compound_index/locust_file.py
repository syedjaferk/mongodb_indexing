
import random
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser
from faker import Faker

log = logging.getLogger("rest-api-short-urls")
fake = Faker()

class LocustClient(FastHttpUser):
    wait_time = constant(0)
    host = "http://localhost:8000/category"


    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)


    @task
    def test_1(self):

        try:
            category = fake.random_element(["electronics", "toys", "vegetables", "fruits", "fish", "meat", "furnitures", "rice", "dress", "entertainment"])
            rating = fake.random_element([1, 2, 3, 4, 5])
            with self.client.get(f'/{category}/rating/{rating}', name='get by category and rating') as resp_of_api:
                if resp_of_api.status_code == 200:
                    log.info("API call resulted in success.")
                else:
                    log.error("API call resulted in failed.")
             
        except Exception as e:
            log.error(f"Exception occurred! details are {e}")
    
    # @task
    # def test_2(self):

    #     try:
    #         category = fake.random_element(["electronics", "toys", "vegetables", "fruits", "fish", "meat", "furnitures", "rice", "dress", "entertainment"])
    #         with self.client.get(f'/{category}', name='get by category') as resp_of_api:
    #             if resp_of_api.status_code == 200:
    #                 log.info("API call resulted in success.")
    #             else:
    #                 log.error("API call resulted in failed.")
             
    #     except Exception as e:
    #         log.error(f"Exception occurred! details are {e}")

    # @task
    # def test_3(self):

    #     try:
    #         category = fake.random_element(["electronics", "toys", "vegetables", "fruits", "fish", "meat", "furnitures", "rice", "dress", "entertainment"])
    #         price = round(random.uniform(5.0, 500.0))
    #         with self.client.get(f'/{category}/price/{price}', name='get by category and price') as resp_of_api:
    #             if resp_of_api.status_code == 200:
    #                 log.info("API call resulted in success.")
    #             else:
    #                 log.error("API call resulted in failed.")
             
    #     except Exception as e:
    #         log.error(f"Exception occurred! details are {e}")