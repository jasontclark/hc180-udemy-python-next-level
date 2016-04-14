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

# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string
#from __future__ import division

import re, string, itertools

def solve(rawFormula):
    """
    rawFormula = "SEND + MORE = MONEY"
    Test all possible translations between Character string and Numbered String
    Return the Solution to the puzzle or None is no solution is found.
    """
    for formula in fill_in(rawFormula):
        if valid(formula):
            return formula
    return None

def fill_in(rawFormula):
    """
    Generate all possible translations between Character string and Numbered String.
    """
    letters = ''.join(set(re.findall('[A-Z]', rawFormula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield rawFormula.translate(table)


def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    1/0 = 1 --> ERROR, Dividing by Zero
    """
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False

print solve('ODD + ODD == EVEN')

#print solve('SEND + MORE == MONEY')
