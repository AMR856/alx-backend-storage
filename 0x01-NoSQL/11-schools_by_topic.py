#!/usr/bin/env python3
"""Just do it"""


def schools_by_topic(mongo_collection, topic):
    """The function's here"""
    school_collections = list(mongo_collection.find({"topics": topic}))
    return school_collections
