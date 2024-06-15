#!/usr/bin/env python3
"""This file will contain some really big stuff"""
import redis
from typing import Union
import uuid


class Cache:
    """A caching class I think"""
    def __init__(self) -> None:
        """The init method is here"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """I'm storing in here as you can see"""
        the_key = str(uuid.uuid4())
        self.__redis.set(the_key, data)
        return the_key
