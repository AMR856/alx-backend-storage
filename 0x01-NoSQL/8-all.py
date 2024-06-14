#!/usr/bin/env python3
"""You forgot to do something lol"""


def list_all(mongo_collection):
    """A function to list things"""
    docs = list(mongo_collection.find())
    if len(docs) == 0:
        return []
    return docs
