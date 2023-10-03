#!/usr/bin/env python3
"""module that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all documents"""
    documents = [doc for doc in mongo_collection.find()]
    return documents
