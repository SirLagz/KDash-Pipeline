#!/usr/bin/python

def update_mongo_collection(client,database,collection,post,id='_id',server='localhost',port=27017):
    from pymongo import MongoClient

#    client = MongoClient(server,port)
    database = client[database]
    collection = database[collection]

    print("Upserting "+post[id])

    try:
        id = collection.update({id:post[id]}, post, upsert=True)
        return id
    except err:
        return err


def check_connection(server='localhost',port=27017):
    from pymongo import MongoClient

    try:
        client = MongoClient(server,port)
        client.server_info()
        return 1
    except:
        return 0


def get_connection(server='localhost',port=27017):
    from pymongo import MongoClient
    client = MongoClient(server,port)
    return client
