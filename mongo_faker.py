import random
from faker import Faker
from pymongo import MongoClient
import uuid
import json


client = MongoClient('mongodb://localhost:27017/')
db = client['product_db']
product_collection = db['products']
product_collection_no_index = db['products2']
sku_ids = []

fake = Faker()
for _ in range(100000):
    sku = str(uuid.uuid4())
    product = {
        "name": fake.word(),
        "category": fake.word(),
        "price": round(random.uniform(5.0, 500.0)),
        "in_stock": fake.boolean(),
        "created_at": fake.date_time_this_decade(),
        "sku": sku,
        "createdAt": fake.date_time_this_year(),
        "attributes": {"color": fake.color_name(), "size": fake.random_element(["S", "M", "L", "XL"])},
        "discount": random.choice([None, round(random.uniform(1.0, 100.0))])  # Some products have discount
    }
    product_collection.insert_one(product)
    product_collection_no_index.insert_one(product)
    sku_ids.append(sku)

with open('db_data.json', 'w') as f:
    json.dump({'ids': sku_ids}, f)