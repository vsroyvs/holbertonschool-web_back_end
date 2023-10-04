#!/usr/bin/env python3
"""module that returns the list documents having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """documents list"""
    document_finded = mongo_collection.find({'topics': topic})
    return document_finded
