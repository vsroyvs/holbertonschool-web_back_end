#!/usr/bin/env python3
"""module  that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    documents = mongo_collection.insertOne(kwargs)
    
    return documents.get('_id')
