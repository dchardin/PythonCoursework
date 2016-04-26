#!/bin/python

# -----------------------------------------------------------------------------
# Cents4pay.py
# By dchardin <donnie@fedoraproject.org>
# -----------------------------------------------------------------------------
# Instructions
# -----------------------------------------------------------------------------

'''
 
Design a program that calculates the amount of money a person would earn
over a period of time if his/her salary is one penny the first day, 
two pennies the second day, and continues to double each day. 
The program should ask the user for the number of days. Display a table 
showing what salary was for each day, and then show the total pay at the 
end of the period. The output should be displayed in a dollar amount, 
not the number of pennies. 

For example if user enters 5 for total days worked, the output should be 
similar as:

Day                        Daily Pay

1                             $0.01

2                             $0.02

3                             $0.04

4                             $0.08

5                             $0.16

Total Pay			$0.31 

'''

# Note: If any employer offers you this arrangement, TAKE IT!!!!!!!


# -----------------------------------------------------------------------------
# Initialize Variables
# (not necessary in this language, but I think it is best practice)
# -----------------------------------------------------------------------------

counter = 0

salary = 0.01

daystowork = 0

earnings = 0

day = 0

total = 0

totalearnings = 0


# ------------------------------------------------------------------------------
# Operations
# ------------------------------------------------------------------------------


daystowork = float(input("How many days would you like to work?: "))


print "On day %s" % day
print "Your earnings are: "'${:,.2f}'.format(earnings)


counter += 1
day = counter

earnings = salary

print "On day %s" % day
print "Your earnings are: "'${:,.2f}'.format(earnings)

totalearnings = totalearnings + earnings

while counter != daystowork:
    counter += 1
    day = counter
    earnings = earnings * 2.0

    print "On day %s" % day
    print "Your earnings are: "'${:,.2f}'.format(earnings)

    totalearnings = totalearnings + earnings

print "Your total is: "'${:,.2f}'.format(totalearnings)





