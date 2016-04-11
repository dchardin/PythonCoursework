#!/bin/python

# ===============================================================================
# tiptaxcalc.py
# By dchardin <donnie@fedoraproject.org>

# Assignment for 4/10/16:
# Write a program that calculates the total amount of a meal purchased at a
# restaurant. The program should ask user to enter the charge for the food,
# tip percentage, and then calculate and display 7 percent of the food charge as
# sales tax amount, tip amount, and the total amount.

# ==============================================================================

# ------------------------------------------------------------------------------
# import necessary modules
# ------------------------------------------------------------------------------

from sys import argv

# ------------------------------------------------------------------------------
# Initialize Variables
# (not necessary in this language, but I think it is best practice)
# ------------------------------------------------------------------------------

MealPrice = 0.0

TaxPercent = 0.07

TipPercent = 0.0

TipAmount = 0.0

TaxAmount = 0.0

MealPlusTaxTotal = 0.0

Total = 0

# ------------------------------------------------------------------------------
# Calculations
# ------------------------------------------------------------------------------

MealPrice = float(input("How much did your meal cost?"))

TipPercent = float(input("Enter the percentage that you would like to tip \ "
                         "Please enter in decimal form \ "
                         "example: 15% would be 0.15"))

TipAmount = MealPrice * TipPercent

TaxAmount = MealPrice * TaxPercent

MealPlusTaxTotal = MealPrice + TaxAmount

Total = MealPlusTaxTotal + TipAmount

# ------------------------------------------------------------------------------
# Output
# ------------------------------------------------------------------------------

print "you should tip this amount:"
print TipAmount

print "you are paying this amount in tax:"
print TaxAmount

print "your total amount to pay is:"
print Total

