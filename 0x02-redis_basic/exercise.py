#!/usr/bin/env python3
"""
Redis module
"""
import sys
from uuid import uuid4

import redis

from typing import Union, Callable

class Cache:
    """
    Cache redis class
    """

    def __init__(self):
        """
        constructor of the redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key (e.g. using uuid),
         store the input data in Redis using the
          random key and return the key.
        :param data:
        :return:
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
    @count_calls
    @call_history

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """
        convert the data back
        to the desired format
        :param key:
        :param fn:
        :return:
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """get a string"""
        return self.decode("utf-8")
