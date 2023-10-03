#!/usr/bin/env python3
"""module changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """change document in a collection"""
    document_updated = mongo_collection.update_many(
        {'name': name },
        {'$set': {
            'topics': topics
        }}
    )
