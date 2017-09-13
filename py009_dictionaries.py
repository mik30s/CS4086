# -*- coding: utf-8 -*-
"""
Dictionaries
Dictionaries are key-value pair groupings
"""

# make an empty dictionary
di = {}
print di

# the order in whcih pairs are stored in dictionaries is not guranteed
di = {'red':(255,0,0), 'green':(0,255,0)}
print di
print di['red']
print di['green']
# you can update a dictionary with they indexing operator
di['blue'] = 89
print di['blue']
# they can also be updated with the update function
di.update({'yellow':(255,255,0)})
print di

# are dictionaries immutable
di = {1:10}
di[1] = 42
print di
# NB: their keys are immutable 

# the fundamental numeric data types are immutable
a = True
print id(a) 
a = False
print id(a) # different id
# you can try this by looping
# only when you assign can you change an immutable's value

# remember that dictionaries are not ordered
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two','three'], [1,2,3]))
# so all of these are equal
print a == b == c

di = {1:10}
di[1] = 42
print di
# your program will crash because you don't have that key
# in your dictionary
# print di[2]
# so you can use dict.get() to be safe
print di.get('blue')
print di.get('blue', 'not defined')

# You can use dict.keys(), dict.values(), list(), dict.items()
# to destructure your dictionary
di = {'red':(255,0,0), 'green':(0,255,0)}
print di.keys()
print di.values()
print
print list(di)
print di.items()
# items() and dict perform different functions
# items() and zip perform the same function

# remove stuff from lists is simple
# you can use del() and dict.pop()


