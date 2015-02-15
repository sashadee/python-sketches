#!/usr/bin/env python

"""
Simple code snippet to test git integration.
"""
__author__ = "sasha"

import os
import time
import turtle

print """
This program draws shapes
Question time:
"""
#square_count = raw_input()
shape_sides = int(raw_input("How many sides should the shape have?:"))


if (int(shape_sides) % 2 == 0):
    print "Nice number, lets go!"
elif (int(shape_sides) % 1 == 0):
    print "I cant draw shapes with an odd number of sides just yet"
    os._exit(1)
else:
    print "Bad number - please try again"
    os._exit(1)


#geometry
shape_length = 50
shape_width = 50

window = turtle.Screen()
my_turtle = turtle.Turtle()

#draw the shape
shape_internal_angles = 360/shape_sides

for i in range(0,shape_sides/2):
    my_turtle.forward(shape_length)
    my_turtle.left(shape_internal_angles)
    my_turtle.forward(shape_width)
    my_turtle.left(shape_internal_angles)

turtle.done()

# Some versions of IDLE apparently need this :)
# os._exit(1)
