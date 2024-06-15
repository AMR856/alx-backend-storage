#!/usr/bin/env python3
"""This file will contain some really big stuff"""
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps
import uuid


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """A caching class I think"""
    def __init__(self) -> None:
        """The init method is here"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """I'm storing in here as you can see"""
        the_key = str(uuid.uuid4())
        self._redis.set(the_key, data)
        return the_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """The getter"""
        the_returned_object = self._redis.get(key)
        if the_returned_object is None:
            return None
        if fn is not None:
            the_returned_object = fn(the_returned_object)

        return the_returned_object

    def get_str(self, key: str) -> str:
        """String getter"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Integer getter"""
        return self.get(key, lambda x: int(x))
