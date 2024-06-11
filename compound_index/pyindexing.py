from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient('mongodb://localhost:27017/')
db = client['product_db']
collection = db['products2']

# Usecase 

# Find products in a specific category and sort by rating and then by price. 
# Find products in a specific category with a specific rating range and sorted by price.

# collection.create_index([('category', 1), ('price', 1), ('rating', 1)])

res = collection.find({"category": 'electronics', 'rating': {'$gte': 1}},
                {'_id':0}).sort('price', ASCENDING).explain()
import json
print(json.dumps(res))