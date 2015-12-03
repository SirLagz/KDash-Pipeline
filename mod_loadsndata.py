#!/usr/bin/python

def update_mongo_collection(database,collection,post,id='_id',server='localhost',port=27017):
    from pymongo import MongoClient

    client = MongoClient(server,port)
    database = client[database]
    collection = database[collection]
    id = collection.update({id:post[id]}, post, upsert=True)

    return id
