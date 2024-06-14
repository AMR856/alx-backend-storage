#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    """Here we insert an object"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
