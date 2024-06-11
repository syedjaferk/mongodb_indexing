from fastapi import FastAPI, HTTPException
from pymongo.mongo_client import MongoClient

app = FastAPI()

# Mongo Db Connection
MONGO_CONN_STR = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONN_STR)
db = mongo_client['product_db']
collection = db['products2']

@app.get("/ids/{id_val}")
def read_item(id_val: str):
    res = collection.find_one({"sku": id_val}, {'_id':0})
    if res['sku'] == id_val:
        return {"status": "success"}
    else:
        return {"status": "failure"}