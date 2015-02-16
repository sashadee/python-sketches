#!/usr/bin/env python

"""
Draws a simple geometric shape based on input parameters
Now with added support for odd sided shapes
"""
__author__ = "sasha"

import os
import turtle


print """
This program draws shapes
Question time:
"""
#square_count = raw_input()
shape_sides = int(raw_input("How many sides should the shape have?:"))

if isinstance(shape_sides, (int,float)):
    print "Nice number, lets go!"
else:
    print "Bad number - please try again"
    os._exit(1)


#geometry
shape_length = 15

window = turtle.Screen()
my_turtle = turtle.Turtle()

#draw the shape - actual is the real angle
shape_internal_angle_actual = ((shape_sides - 2) * 180) / float(shape_sides)
shape_internal_angle_for_turtle = 180 - shape_internal_angle_actual

print "drawing a shape with %i sides and an internal angle of %i" % (shape_sides, shape_internal_angle_actual)

if (int(shape_sides) % 2 == 0):
    #draw shape with even number of sides
    for i in range(0,shape_sides):
        my_turtle.forward(shape_length)
        my_turtle.left(shape_internal_angle_for_turtle)

    #draw shape with odd number of sides
elif (int(shape_sides) % 1 == 0):

    for i in range(0,(shape_sides)):
        my_turtle.forward(shape_length)
        my_turtle.left(shape_internal_angle_for_turtle)
        print "%f %f" % (shape_sides, shape_internal_angle_for_turtle)

turtle.done()

# Some versions of IDLE apparently need this :)
# os._exit(1)
