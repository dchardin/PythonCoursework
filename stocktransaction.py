#!/bin/python

# ===============================================================================
# stocktransaction.py
# By dchardin <donnie@fedoraproject.org>

# Assignment for 4/10/16:

# Last month Joe purchased some stock in Acme software, Inc. Here are the details
# of the purchase:
#
#
#    The number of shares that Joe purchased was 2,000
#    Joe paid $40.00 per share
#    Joe paid stockbroker 3 percent as commission
#
# Two weeks later, Joe sold the above stock, and here are details of the sale:
#
#    The number of shares that Joe sold was 2,000
#    Joe sold the stock for $42.75  per share
#    Joe paid stockbroker 3 percent as commission
#
# Write a program that displays the following information:
#
#
#    The amount of money Joe paid for the stock
#    The amount of commission Joe paid when he bought the stock
#    The amount that Joe sold the stock for
#    The amount of commission Joe paid when he sold the stock
#    Display the amount of money that Joe had left when he sold
#    the stock and paid his broker (both times).
#    If the amount is positive, then Joe made a profit.
#    If the amount is negative, then Joe lost money.
#
# ==============================================================================



# ------------------------------------------------------------------------------
# import necessary modules
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Initialize Variables
# (not necessary in this language, but I think it is best practice)
# ------------------------------------------------------------------------------

SharesPurchased = 0.0

AmtPaidPerShare = 0.0

CommissionPercentage = 0.0

PaidWithoutCommission = 0.0

CommissionPaid = 0.0

TotalPaid = 0.0

SharesSold = 0.0

AmtSoldPerShare = 0.0

SaleAmount = 0.0

EarnedWithoutCommission = 0.0

CommissionPaidSale = 0.0

TotalEarned = 0.0

ProfitNoProfit = 0.0

# ------------------------------------------------------------------------------
# Calculations
# ------------------------------------------------------------------------------

SharesPurchased = float(input("How many shares did you purchase? \n "
"enter in 0.0 form: "))

AmtPaidPerShare = float(input("How much did you pay per share? \n"
"enter in 0.0 form: "))

CommissionPercentage = float(input("What percentage is your stockbroker \n"
"Charging per transaction? enter in 0.00 form: "))

PaidWithoutCommission = AmtPaidPerShare * SharesPurchased

CommissionPaid = PaidWithoutCommission * CommissionPercentage

TotalPaid = CommissionPaid + PaidWithoutCommission

SharesSold = float(input("How many shares did you sell? \n "
"enter in 0.0 form: "))

AmtSoldPerShare = float(input("How much did you sell each share for? \n"
"enter in 0.0 form: "))

EarnedWithoutCommission = AmtSoldPerShare * SharesSold

CommissionPaidSale = EarnedWithoutCommission * CommissionPercentage

TotalEarned = EarnedWithoutCommission - CommissionPaidSale

ProfitNoProfit = TotalEarned - TotalPaid
# ------------------------------------------------------------------------------
# Output
# ------------------------------------------------------------------------------

print "You paid the following for the shares:"
print PaidWithoutCommission

print "You paid the following in commissions to your stockbroker for the purchase:"
print CommissionPaid

print "In total, you paid:"
print TotalPaid

print "You sold your shares for the amount of:"
print EarnedWithoutCommission

print "You paid the following in commissions to your stockbroker for the sale:"
print CommissionPaidSale

print "In total, your revenue is: "
print TotalEarned

if ProfitNoProfit > 0:
    print "You have earned a profit of: %s." % ProfitNoProfit
elif ProfitNoProfit == 0:
    print "You have broken even"
else: print "You have lost this amount: %s." % ProfitNoProfit