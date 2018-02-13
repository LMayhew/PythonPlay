#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:57:41 2018

@author: lmayhew2002
"""

# Google Python: Lists
colors = ['red', 'blue', 'green']
print(colors[0])  # red
print(colors[2])  # green
print(len(colors))  # 3

# these point to same place, not copy!!
b = colors
print(b)
b[2] = 'chartruse'
print(colors)  # ['red', 'blue', 'chartruse']

# Concatenate lists
addNum = [1, 2] + [3, 4]
print(addNum)

# For and In
# for var in list
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  # 30

list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')

for i in range(100):  # 0 to 99
    print(i)

i = 0
a = 'supercalifragilicious'
while i < len(a):
    print(a[i])
    i = i + 3

####################
# List methods
myList = [1, 2, 3, 4, 5]
myList.append(6)
print(myList)  # [1, 2, 3, 4, 5, 6]

myList.insert(3, 45)  # after 3, insert 45
print(myList)  # [1, 2, 3, 45, 4, 5, 6]

myList1 = [77, 78, 79]
myList += myList1
print(myList)  # 1, 2, 3, 45, 4, 5, 6, 77, 78, 79]

print(myList.index(45))   # 3

myList.reverse()  # does not return it, do it then use it
print(myList)  # [79, 78, 77, 45, 6, 5, 4, 3, 2, 1]
print(myList.reverse())  # None

print(myList.pop(1))  # 2
print(myList)  # [1, 3, 4, 5, 6, 45, 77, 78, 79]

########
# list build up
list = []
list.append('a')
list.append('b')

########
# list slices
list = ['a', 'b', 'c', 'd']
print(list[1:-1])  # ['b', 'c']
list[0:2] = 'z'    # replace [a,b] with z
print(list)  # ['z', 'c', 'd']

# next do list1.py
