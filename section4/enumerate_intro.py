#!/usr/bin/env python
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

## enumerate(sequence)

##      Return an enumerate object. sequence must be a sequence, an iterator,
##      or some other object which supports iteration. The next() method of the
##      iterator returned by enumerate() returns a tuple containing a count
##      (from start which defaults to 0) and the values obtained from iterating
##      over sequence:

for (i, d) in enumerate("ONE"):
    print (i,d)
    print '{}*{}'.format(10**i, d)
    print ""
