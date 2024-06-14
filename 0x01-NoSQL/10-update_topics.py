#!/usr/bin/env python3
"""Just do it"""


def update_topics(mongo_collection, name, topics):
    """The function's here"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
