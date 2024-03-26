
import pymongo
if __name__=="__main__":
    print("Wlcome to pymongo")
    client= pymongo.MongoClient("mongodb://username:password@localhost:27017")
    print(client)
    # client = pymongo.MongoClient("localhost", 27017)
    # db = client.test_database
    # db.test_table