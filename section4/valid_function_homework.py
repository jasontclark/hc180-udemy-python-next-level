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


# - solve   --> Runs thru all possible combinations testing each for valid
# - fill_in --> Create a new formula replacing letters with numbers
# - valid   --> Tests our filled-in string

import re

def solve(rawformula):
    """
    Test all possible translations betwee Character string and Numbered String
    Return the Solution to the puzzle or None if no solution is found.
    """
    for formula in fill_in(rawFormula):
        if valid(formula):
            return formula
    return None


def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evalutates as True.
    Returns True or False
    """
    try:
        return not re.search(r'\b0[0-9]', forumla) and eval(formula) is True
    except ArithmeticError:
        return False
    except:
        return False

print valid('1+1==2')
