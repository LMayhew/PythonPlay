#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 06:23:27 2018

@author: lmayhew2002
"""

# Google Python Dict & Files
dict = {}  # empty, notice brace not bracket
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict)  # {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}
print(dict['a'])  # alpha
dict['a'] = 6
print(dict['a'])  # 6
'a' in dict  # True
print(dict['z'])  # key error
if 'z' in dict: print(dict['z'])
print(dict.get('z'))  # None

#################
# methods
# default - iterate over dict iterates over keys
# keys are in random order
for key in dict: print(key)  # a, g, o
for key in dict.keys(): print(key)  # same
print(dict.keys())    # returns list: dict_keys(['a', 'g', 'o'])
print(dict.values())  # returns list: dict_values([6, 'gamma', 'omega'])

# loop over keys in sorted order
for key in sorted(dict.keys()):
    print(key, dict[key])   # a 6, g gamma, o omega

print(dict.items())  # dict_items([('a', 6), ('g', 'gamma'), ('o', 'omega')])

# loop over items
for k, v in dict.items(): print(k, '>', v)

##########
# format
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash
print(s)  # I want 42 copies of garfield

##########
# del (like rm)
var = 6
del var

list = ['a', 'b', 'c', 'd']
del list[0]
print(list)  # ['b', 'c', 'd']
del list[-2:]
print(list)  # ['b']

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b']
print(dict)  # {'a': 1, 'c': 3}

###########
# Files
f = open('alice.txt', 'r')  # read
for line in f:
    print(line,)  # suppresses print's \n
f.close()

f = open('alice.txt', 'r')  # read
tmp = f.read()  # as char string
f.close()
print(tmp[0]) 


## Bug here?
f = open('tmpFile.txt', 'w')
print('a string to write', file=f)
f.close
f = open('tmpFile.txt', 'r')
for line in f: print(line,)
f.close()

