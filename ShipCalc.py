#!/bin/python


# -----------------------------------------------------------------------------
# ShipCalc.py
# By dchardin <donnie@fedoraproject.org>
# -----------------------------------------------------------------------------
# Instructions
# -----------------------------------------------------------------------------
#
# Program 1 Create a Shipping Charges Program for the Fast Shipping Company 
# in Python (50 points): The Fast Shipping Company charges the following rates:
#
# Weight of Package	Rate per pound
#
# Weight <= 2		$1.10
# 2 < Weight <= 6	$2.20
# 6 < Weight <= 10	$3.70
# 10 > Weight		$3.80
#
# Implement the task in Python, ask user to enter the weight of a package 
# and then display the shipping charge. 
#
# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

lbsOver10Price = 3.80

lbs10orlessButOver6Price = 3.70

lbs6orlessButOver2Price = 2.20

lbs2orLessPrice = 1.10

weightInlbs = 0.0

# ------------------------------------------------------------------------------
# Calculations
# ------------------------------------------------------------------------------


weightInlbs = float(input("Enter your weight in lbs: "))


# Special thanks to Justin Barber on StackOverflow.com, who helped me to come up
# with a means to format my ouput in dollar form with
# '${:,.2f}'.format(FloatVarForFormattingHere)
#
# "The :, adds a comma as a thousands separator, and the .2f limits the string
# to two decimal places (or adds enough zeroes to get to 2 decimal places, as
# the case may be) at the end."
#
#                           -Justin Barber

if weightInlbs > 10.0:
    print "Your postage will be: "'${:,.2f}'.format(lbsOver10Price)
elif weightInlbs > 6 and weightInlbs <= 10:
    print "Your postage will be: "'${:,.2f}'.format(lbs10orlessButOver6Price)
elif weightInlbs > 2 and weightInlbs <= 6:
    print "Your postage will be: "'${:,.2f}'.format(lbs6orlessButOver2Price)
elif weightInlbs > 0 and weightInlbs <= 2:
    print "Your postage will be: "'${:,.2f}'.format(lbs2orLessPrice)










