#!/usr/bin/env python3
"""module that that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == '__main__':
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient.logs
    mycol = mydb.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    x = mycol.count_documents({})

    print(f"{x} logs")
    print("Methods:")
    for i in method:
        print(f"method {i}: {mycol.count_documents({'method': i})}")
    print(f"{mycol.count_documents({'method': 'GET', 'path': '/status'})} status check")
