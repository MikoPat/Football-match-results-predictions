import pymongo
import pandas as pd
from credencials_mongo import user_name, password


def uploadMongo(data_to_mongo):

    client_link = "mongodb+srv://"+ user_name + ":" + password + "@football.cvyivdz.mongodb.net/"

    client = pymongo.MongoClient(client_link)

    db = client.football
    collection = db.predictions

    result = collection.insert_one(data_to_mongo)

    print("Inserted document ID:", result.inserted_id)

    client.close()

def getDataFromMongo():

    mongo_url = "mongodb+srv://"+ user_name + ":" + password + "@football.cvyivdz.mongodb.net/"
    database_name = "football"
    collection_name = "predictions_italy"

    client = pymongo.MongoClient(mongo_url)
    database = client[database_name]
    collection = database[collection_name]

    cursor = collection.find()
    documents_list = list(cursor)

    client.close()

    df = pd.DataFrame(documents_list)

    return df