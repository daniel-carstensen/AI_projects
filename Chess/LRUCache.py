# Author : Daniel Carstensen
# Date : 10/26/2022
# File name : LRUCache.py
# Class : COSC76
# Purpose : Implementation of LRU cache

from collections import OrderedDict


# LRUCache class
class LRUCache:

    # max_size: maximum number if key-value pairs to be stored in cache
    # cache: ordered dictionary
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()

    # return the value corresponding to the input key and move the key-value pair to the end of the dictionary
    # if key doesn't have a value, return None
    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache.get(key)

    # insert a new key-value pair or update the value
    # if maximum size is reached, pop the LRU key-value pair
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

