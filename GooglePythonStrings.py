#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:04:48 2018

@author: lmayhew2002
"""
# Google Python: Strings
s = 'hi'
print(s[1])
print(len(s))
print(s + ' there')

pi = 3.14
print('The value of pi is ' + pi)       # error
print('The value of pi is ' + str(pi))

raw = r'this\t\n and that'  # as is
print(raw)

multi = """It was the best of times.
It was the worst of times."""

print(multi)  # multilines

########################
# String Methods
myStr = 'THIS IS UPPER'
myStr1 = 'this is lower'

print(myStr.lower())   # this is upper
print(myStr1.upper())  # THIS IS LOWER

myStr2 = '   spaces  '
print('[' + myStr2.strip() + ']')

myStr3 = '3450'
myStr3.isalpha()  # F
myStr3.isdigit()  # T

myStr4 = '345.0'
myStr4.isdigit()  # F

myStr4.replace('.', 'HI')  # '345HI0'

myStr5 = 'aaa.bbb.ccc'
myStr5.split('.')  # ['aaa', 'bbb', 'ccc']

#########################
# String Slices
s = "Hello"     # 0 1 2 3 4 = H E L L O
# -5 -4 -3 -2 -1 = H E L L O

# From beginning
s[1:4]  # ell, index 1 to 4 not incl end
s[1:]   # ello, omit index = start / end
s[:]    # whole, as copy
s[1:100]  # ello, too big truncated to string length

# From end
s[-1]   # o, last
s[-4]   # e, 4th from last
s[:-3]   # He, beg to 3rd (not incl)
s[-3:]  # llo, 3rd fr end to end

# Truism
n = 3  # arbitrary
s[:n] + s[n:] == s  # True, 1 to n (not incl n), n to end (incl n)

#########################
# String %
# "3 little pigs come out or I'll huff and puff"
text = "%d little pigs come out or I'll %s and %s" % (3, 'huff', 'puff')

# mulitple lines
text = ("%d little pigs come out or I'll %s and %s" %
        (3, 'huff', 'puff'))

#######################
# if statment - notice the colons and tabs
# dont put boolean test in parans
speed = 85
mood = "happy"
if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket.")
        # write_ticket()
    else:
        print("Let's try to keep it under 80 ok?")

# next do string1.py