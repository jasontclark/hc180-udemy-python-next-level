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
""" re_search.py - searches a string for a leading zero."""
import re

def noFirstZero(formula):
    """ uses a regular expression search to look for a leading zero. """
    return not re.search(r'\b0[0-9]', formula)

def test_noFirstZero(L):
    """ runs a quick test. """
    for formula in L:
        print formula, noFirstZero(formula)

""" Test """
L = ['123', '406', '023', '543 0543', '087 65', '00', '432 123']
test_noFirstZero(L)
