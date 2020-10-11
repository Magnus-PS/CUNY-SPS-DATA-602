#!/usr/bin/env python
# coding: utf-8

# In[16]:


#These exercises were derived from Ben Stephenson's 'The Python Workbook'

#The aim of using this text is to refine my own Python programming capabilities via:
##(1) completing the exercises therein, and
##(2) comparing solutions with those provided by the author


#Exercise 6: Tax and Tip

#
#Read the cost of a meal from the user, calculate tax and tip, and then display these values along with the grand total with 2 decimal places.
#

cost = float(input("Please enter the cost of your meal (minus $-sign): "))
tax = cost * 0.08
tip = cost * 0.18

print("Tax: $", "{:.2f}".format(tax), ".","Tip: $", "{:.2f}".format(tip), ".")
print("Total: $", "{:.2f}".format(cost + tax + tip), ".")


#Exercise 7: Sum of the First n Positive Integers

#
# Read integer n from user then compute and display the sum of all integers from 1 to n.
#

n = int(input("Enter an integer: "))
sum = (n * (n+1)) / 2

#Display the sum
print("Sum of integers upto n is:", int(sum))


#Exercise 8: Widgets and Gizmos

#
# Read the number of widgets and gizmos from user then compute and display the total weight of the order.
#

widgets = int(input("Enter the number of widgets in the order: "))
gizmos = int(input("Enter the number of gizmos in the order: "))

total_weight = (75 * widgets) + (112 * gizmos)

#Display the sum
print("The total weight of the order is", int(total_weight), "grams.")


#Exercise 9: Compound Interest

#
# Read the amount of $ deposited into the account from the user then compute and display the amount in savings after 1, 2, and 3 years. Display amounts rounded to 2 decimal places.
#

deposit = float(input("Enter the amount deposited into your account (minus $-sign): "))

savings_yr1 = deposit * 1.04
savings_yr2 = savings_yr1 * 1.04
savings_yr3 = savings_yr2 * 1.04

print("Year 1 savings: $","{:.2f}".format(savings_yr1))
print("Year 2 savings: $","{:.2f}".format(savings_yr2))
print("Year 3 savings: $","{:.2f}".format(savings_yr3))

#Exercise 10: Arithmetic

#
# Read two integers from a user and compute and display a number of arithmetic operations using these integers
#

a = int(input("Enter an integer value (a): "))
b = int(input("Enter another integer value (b): "))

sum = a + b
difference = a - b
product = a * b

print("The sum of a and b (a+b) is :", sum)
print("The difference between a and b (a-b) is :", difference)
print("The product of a and b (a*b) is:", product)


# In[ ]:





# In[ ]:




