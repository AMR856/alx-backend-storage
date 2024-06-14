#!/usr/bin/env python3
def list_all(mongo_collection):
    """A function to list things"""
    docs = list(mongo_collection.find())
    if len(docs) == 0:
        return []
    return docs
