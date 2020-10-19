#!/usr/bin/env python
# coding: utf-8

# In[15]:


#These exercises were derived from Ben Stephenson's 'The Python Workbook'

#The aim of using this text is to refine my own Python programming capabilities via:
##(1) completing the exercises therein, and
##(2) comparing solutions with those provided by the author


#--->Section: If Statement Exercises<---#

#Exercise 38: Month Name to Number of Days

#
#The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month
#from the user as a string. Then your program should display the number of days in that month. Display "28 or 29 days" for
#February so that leap years are addressed.
#

mo_name = input("Please enter the name of the month: ")

#31 days: January, March, May, July, August, October, December
#30 days: April, June, September, November
#28 or 29 days: February
if mo_name == "February":
    print("There are 28 or 29 days in", mo_name, ".")
elif mo_name == "April" or mo_name == "June" or mo_name == "September" or mo_name == "November":
    print("There are 30 days in", mo_name, ".")
else:
    print("There are 31 days in", mo_name, ".")

    
#--->Section: Loop Exercises<---#

#Exercise 75: Greatest Common Divisor

#
#Write a program that reads two positive integers from the user and uses this algorithm to determine and report their
#greatest common divisor.
#

n = int(input("Please enter your 1st (positive) integer: "))
m = int(input("Please enter your 2nd (positive) integer: "))
d = 0

#initialize d to the samller of m and n
if n > m:
    d = m
else:
    d = n

while (m % d != 0) or (n % d != 0):
    d -= 1

print(str(d))
    

#--->Section: Function Exercises<---#

#Exercise 84: Median of Three Values

#
#Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result.
#Include a main program that reads three values from the user and displays their median.
#

def median(a, b, c):
    order_list = [a, b, c]
    order_list.sort() #sort list in ascending order
    return order_list[1] #return mid / median value

print("The median of the list is:", median(10,-10,30))


#--->Section: List Exercises<---#

#Exercise 112: Below and Above Average

#
#Write a program that displays the average of all of the values entered by the user. Then the program should display 
#all of the below average values, followed by all of the average values (if any), followed by all of the above average 
#values. An appropriate label should be displayed before each list of values.
#

#Read numbers from user until a blank line is entered.
num_list = []

while True:
    number = input("Please enter a number to add to your list and nothing to finish the list: ")
    
    if number == "":
        break
    else:
        num_list.append(int(number))

#Calculate average value
avg_val = sum(num_list) / len(num_list)

#Display average value
print("The average value is: ", avg_val)

greater_list = []
lesser_list = []

#Display all below average values
for x in num_list:
    if x > avg_val:
        greater_list.append(x)
    else:
        lesser_list.append(x)

print("The below average values are:", lesser_list)
print("The above average values are:", greater_list)


# In[ ]:




