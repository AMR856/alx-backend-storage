#!/usr/bin/env python3
"""This file will contain some really big stuff"""
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps
import uuid


def count_calls(method: Callable) -> Callable:
    """Counter here"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """History repeater"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """I don't remember what does this function do"""
    print(method)
    if method is None or not hasattr(method, '__self__'):
        return
    redis_storage = getattr(method.__self__, '_redis')
    method_qualifed_name = method.__qualname__
    input_key = f'{method_qualifed_name}:inputs'
    output_key = f'{method_qualifed_name}:outputs'
    if redis_storage.exists(method_qualifed_name):
        calls_count = int(redis_storage.get(method_qualifed_name))
    print(f'{method_qualifed_name} was called {calls_count}')
    inputs = redis_storage.lrange(input_key, 0, -1)
    outputs = redis_storage.lrange(output_key, 0, -1)
    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            method_qualifed_name,
            input.decode('utf-8'),
            output.decode('utf-8')
        ))


class Cache:
    """A caching class I think"""
    def __init__(self) -> None:
        """The init method is here"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
