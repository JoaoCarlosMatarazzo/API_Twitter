from pymongo import MongoClient

client = MongoClient("mongodb://dio:dioPlacahost:27017") #exemplo
db = client.my_test
trends_collection = db.trends



