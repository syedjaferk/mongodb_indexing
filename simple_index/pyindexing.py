from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['product_db']
collection = db['products']

collection.create_index([("sku", 1)])

