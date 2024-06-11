from fastapi import FastAPI, HTTPException
from pymongo.mongo_client import MongoClient
from pymongo import ASCENDING, DESCENDING

app = FastAPI()

# Mongo Db Connection
MONGO_CONN_STR = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONN_STR)
db = mongo_client['product_db']
collection = db['products2']

@app.get("/category/{category}/rating/{r_gte}")
def read_item(category: str, r_gte: int):
    res = collection.find({"category": category, 'rating': {'$gte': r_gte}}, {'_id':0}).sort('price', ASCENDING)
    if res:
        return {"status": "success"}

@app.get("/category/{category}")
def read_category(category: str):
    res = collection.find({"category": category}, {'_id':0})
    if res:
        return {"status": "success"}

@app.get("/category/{category}/price/{p_lte}")
def find_category_with_price(category: str, p_lte: int):
    res = collection.find({"category": category, 'price': {'$lte': p_lte}}, {'_id':0})
    if res:
        return {"status": "success"}