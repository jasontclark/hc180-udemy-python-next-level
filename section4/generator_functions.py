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
""" Section 4, Lecture 44 - Generator Functions """

def count(start,end):
    i = start
    while i <= end:
        yield i
        i = i+1

c = count(0,10)

print c
print c.next()
print c.next()
print c.next()

for i in c:
    print i

def count_again(start, end = None):
    i = start
    while i <= end or end == None:
            yield i
            yield -i
            i = i+1

d = count_again(0)
print d

for i in range(100):
    print d.next()
