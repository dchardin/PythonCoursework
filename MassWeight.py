#!/bin/python


# -----------------------------------------------------------------------------
# MassWeight.py
# By dchardin <donnie@fedoraproject.org>
# -----------------------------------------------------------------------------
# Instructions
# -----------------------------------------------------------------------------
#
# Scientists measure an objects mass in kilograms and its weight in newtons.
# Create a Python program that asks user to enter the mass of an object,
# and calculates the newtons of that object using the following formula 
#
# weight = mass * 9.8
#
# And the program should also give a message to the user afterwards:
# 
# "Too light" for objects weighing 100 newtons or less
# "Just right" for objects weighing over 100 newtons but less than 500
# "Too heavy" for objects weighing 500 or more newtons 
#
# 
# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

mass = float(input("Enter mass: "))

weight = mass * 9.8

if weight >= 500.0:
    print "too heavy"
elif weight >= 100.0 and weight < 500.0:
    print "just right"
elif weight <= 100.0:
    print "too light"

