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
section 3 - computer3 simulation code
"""
import fake_database

CACHE = {}

def print_name():
    print str(__name__)

def update_last_multiplied(a, b, result):
    key = 'last_five'

    lastFiveList = CACHE.get(key)

    if lastFiveList:
        if len(lastFiveList) >= 5:
            newList = lastFiveList[1:]
            newList.append('{}x{}={}'.format(a, b, result))
            CACHE[key] = newList
        else:
            lastFiveList.append('{}x{}={}'.format(a, b, result))
            CACHE[key] = lastFiveList
    else:
        CACHE[key] = ['{}x{}={}'.format(a, b, result)]

def last_multiplied_handler():
    """
    Inputs : none
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    key = 'last_five'

    if key in CACHE:
        print 'Last Five = {}'.format(CACHE[key])
        print '*' * 8
        print ' '
    else:
        print 'Russian not Used.'
        print '*' * 8
        print ' '

def multiply_handler(a, b):
    """
    Inputs : a, b representing Number as arguments from the request
    Outputs: The result of those two number being sent thru The
              Russian's Peasant's Algorithm
    """
    cache_key = (a, b)

    if cache_key in CACHE:
        print CACHE[cache_key]
    else:
        result = fake_database.russian(a, b)
        update_last_multiplied(a, b, result)
        CACHE[cache_key] = result
        print 'Latest Result: {}'.format(result)
        last_multiplied_handler()

if __name__ == '__main__':
      multiply_handler(2,6)
      multiply_handler(5,6)
      multiply_handler(10,6)
