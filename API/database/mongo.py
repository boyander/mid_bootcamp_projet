from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
#esta url posteriormente habria que facilitarla como parametro
url =f"mongodb+srv://{username}:{password}@cluster0.l7ahf.mongodb.net/test" 
db = MongoClient().getdatabase('Prueba2')['partidos']
