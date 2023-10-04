#!/usr/bin/env python3
"""module that that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == '__main__':
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient['logs']
    mycol = mydb['nginx']
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    x = mycol.find().count()

    print(f"{x} logs")
    print("Methods:")
    for i in method:
        print(f"method {i}: {mycol.find({'method': i}).count()}")
    print(f"{mycol.find({'method': 'GET', 'path': '/status'}).count()} status check")
