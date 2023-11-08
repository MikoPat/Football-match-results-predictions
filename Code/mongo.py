import pymongo
from credencials_mongo import user_name, password


def uploadMongo(data_to_mongo):

    client_link = "mongodb+srv://"+ user_name + ":" + password + "@football.cvyivdz.mongodb.net/"

    client = pymongo.MongoClient(client_link)

    db = client.football
    collection = db.predictions

    result = collection.insert_one(data_to_mongo)

    print("Inserted document ID:", result.inserted_id)

    client.close()