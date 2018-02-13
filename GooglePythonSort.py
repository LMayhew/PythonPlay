#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 05:58:05 2018

@author: lmayhew2002
"""

# Google Python Sort
a = [5, 1, 4, 3]
print(sorted(a))  # does not change a, [1, 3, 4, 5]
print(a)          # [5, 1, 4, 3]

# Sort w custom key
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs))  # ['aaaa', 'bb', 'ccc', 'd']
print(sorted(strs, key=len))  # ['d', 'bb', 'ccc', 'aaaa']
strs = ['BB', 'aa', 'zz', 'CC']
print(sorted(strs, key=str.lower))  # ['aa', 'BB', 'CC', 'zz']

######################################
# custom function, sort by last letter
strs = ['xc', 'zb', 'yd', 'wa']


# key function takes in 1 val, returns 1 val
def MyFn(s):
    return s[-1]

print(sorted(strs, key=MyFn))  # ['wa', 'zb', 'xc', 'yd']

# Tuples
tuple = (1, 2, 'hi')
print(len(tuple))  # 3
print(tuple[2])  # 'hi
tuple[2] = 'bye'  # tuples are immutable
print(tuple)  # (1, 2, 'hi')
tuple = (1, 2, 'bye')  # this works
print(tuple)  # (1, 2, 'bye')

# size 1 tuple, notice comma
tuple = ('hi',)
print(tuple)  # ('hi',)

# Heres the power: assignment
(x, y, z) = (42, 13, "hike")
print(z)  # hike

#####################
# List comprehensions
nums = [1, 2, 3, 4]
squares = [n*n for n in nums]
print(squares)  # [1, 4, 9, 16]

strs = ['hello', 'and', 'goodbye']
shouting = [s.upper() + '!!!' for s in strs]
print(shouting)  # ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

# add if to filter
nums = [2, 8, 1, 6]
small = [n for n in nums if n <= 2]
print(small)  # [2, 1]

fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
print(afruits)  # ['APPLE', 'BANNANA']

# next do list1.py
