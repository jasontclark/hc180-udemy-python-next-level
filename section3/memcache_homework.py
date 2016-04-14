#!/usr/bin/env python
#
# Copyright 2015 Jason T Clark
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
memcache_homework.py - section 3 homework
"""
class Memcache(object):

    MEMORY = {}

    def __init__(self):
        global MEMORY
        self.CACHE = MEMORY

    def set(self, key, value):
        self.CACHE[key] = value
        return True

    def get(self, key):
        return self.CACHE.get(key)

    def delete(self, key):
        if key in self.CACHE:
            del self.CACHE[key]

    def flush(self):
        self.CACHE.clear()

def test_memcache():
    m = Memcache()
    print m.set('a', '1')
    print m.set('b', '2')
    print m.CACHE
    print m.get('b')
    print m.get('c')
    m.delete('b')
    print m.CACHE
    m.flush()
    print m.CACHE

if __name__ == '__main__':
    test_memcache()
