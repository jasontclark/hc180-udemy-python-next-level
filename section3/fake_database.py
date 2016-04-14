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
Russian Peasant's Algorithm - fake database
"""
import time

def russian(num1, num2):
    x = num1; y = num2    ## Compound Assignment
    z = 0                 ## Acumulator

    while x > 0:          ## While Loop Begins
        if x % 2 == 1:    ## Modulo operator
            z = z + y     ## Acumulate Sum
        y = y << 1        ## Shift Binary Left
        x = x >> 1        ## Shift Binary Right
    return z              ## Return Z

def test_russian():
    start_time = time.time()
    print russian(357, 16)
    print 'Russian Algorithm took %f seconds' % (time.time() - start_time)

    assert russian(357, 16) == 5712

if __name__ == "__main__":
    test_russian()
