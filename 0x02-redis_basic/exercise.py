#!/usr/bin/env python3
"""
Redis module
"""
import sys
from uuid import uuid4

import redis

from typing import Union

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
