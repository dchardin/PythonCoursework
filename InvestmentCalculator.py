#!/bin/python

#===============================================================================
# InvestmentCalculator.py
# By dchardin <donnie@fedoraproject.org>
#===============================================================================
  

'''
Create a program that asks user:

1. enter amount of money invested, number of years investing, and annual 
interest rate in decimal format

2. call a user-defined function to get total value at end of investment 
term(futureValue)

3. call another user defined function to get total interest earned.

4. Display total value and total interest earned at end of the term

Note: Use the following formula to calculate totalFutureValue is:

FutureValue = InvestedAmount*(1 + AnnualInterestRate/12)**(InvestedYears * 12) 

'''


# ------------------------------------------------------------------------------
# import necessary modules
# ------------------------------------------------------------------------------

from __future__ import division

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

def main():

    #Get the Interest, Years, etc,

    AmtInvested = float(input('Enter the amount you wish to invest?'))

    InterestRate = float(input('Enter the interest rate in decimal format'))

    Years = float(input('Enter the number of years'))

    FutureValue = future_value_finder(AmtInvested, InterestRate, Years)

    InterestEarned = interest_earned_finder(FutureValue, AmtInvested)

    print("The future value is:")
    print(FutureValue)
    print("You have earned the following in interest")
    print(InterestEarned)


def head():
    print("Future Value Calculator")

def future_value_finder(invested, intrate, yrs):
    futurevalue = invested * (1 + intrate / 12) ** (yrs * 12)
    return futurevalue

def interest_earned_finder(thefuturevalue, theorigvalue):
    intearned = thefuturevalue - theorigvalue
    return intearned

# ------------------------------------------------------------------------------
# Operations
# ------------------------------------------------------------------------------

main()



























