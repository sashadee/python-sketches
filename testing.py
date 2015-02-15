#!/usr/bin/env python

"""
Simple code snippet to test git integration.
"""
__author__ = "sasha"

#tuples and lists
values = raw_input("input some numbers, seperate with comma:\n")



if values == "":
    print "No number entered, adding some numbers for fun"
    values = "10,9,8,7,6,5,4,3,2,1"

print values

my_list = values.split(",")
my_tuple = tuple(my_list)

print my_list
print my_tuple
