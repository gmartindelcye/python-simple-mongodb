import os   
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB = os.environ.get("MONGO_DB")
breakpoint() 
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db["coleccion_pruebas"]
 
for i in range(10):
    doc = {}
    doc["titulo"] = f"Titulo de pruebas número {i}"
    doc["numero"] = str(i)
    doc["contenido"] = f"Este es el contenido del documento número {i}"
 
    collection.insert_one(doc)
