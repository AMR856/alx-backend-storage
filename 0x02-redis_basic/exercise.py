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

# In this tasks, we will implement a replay function to display the history of calls of a particular function.

# Use keys generated in previous tasks to generate the following output:

# >>> cache = Cache()
# >>> cache.store("foo")
# >>> cache.store("bar")
# >>> cache.store(42)
# >>> replay(cache.store)
# Cache.store was called 3 times:
# Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
# Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
# Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
# Tip: use lrange and zip to loop over inputs and outputs.

# def replay(fn: Callable) -> None:
#     '''Displays the call history of a Cache class' method.
#     '''
#     if fn is None or not hasattr(fn, '__self__'):
#         return
#     redis_store = getattr(fn.__self__, '_redis', None)
#     if not isinstance(redis_store, redis.Redis):
#         return
#     fxn_name = fn.__qualname__
#     in_key = '{}:inputs'.format(fxn_name)
#     out_key = '{}:outputs'.format(fxn_name)
#     fxn_call_count = 0
#     if redis_store.exists(fxn_name) != 0:
#         fxn_call_count = int(redis_store.get(fxn_name))
#     print('{} was called {} times:'.format(fxn_name, fxn_call_count))
#     fxn_inputs = redis_store.lrange(in_key, 0, -1)
#     fxn_outputs = redis_store.lrange(out_key, 0, -1)
#     for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
#         print('{}(*{}) -> {}'.format(
#             fxn_name,
#             fxn_input.decode("utf-8"),
#             fxn_output,
#         ))

def replay(method : Callable) -> None:
    if method is None or not hasattr(method, '__self__'):
        return
    redis_storage = getattr('fn.__self__', '_redis', None)
    method_qualifed_name = method.__qualname__
    input_key = f'{method_qualifed_name}:inputs'
    output_key = f'{method_qualifed_name}:outputs'
    if redis_storage.exists(method_qualifed_name):
        calls_count = redis_storage.get()
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
