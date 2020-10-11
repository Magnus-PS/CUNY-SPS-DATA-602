#!/usr/bin/env python
# coding: utf-8

# In[8]:


#These exercises were derived from Ben Stephenson's 'The Python Workbook'

#The aim of using this text is to refine my own Python programming capabilities via:
##(1) completing the exercises therein, and
##(2) comparing solutions with those provided by the author


#Exercise 1: Mailing Address

#
#Display a person's complete mailing address
#

print("Norm Norwald")
print("37 Middle Norm Blvd")
print("Normaltown, GA 30602")


#Exercise 2: Hello

#
#Ask user to enter name and display it back with a preceding "Hello"
#

name = input("Please enter your name: ")
print("Hello " + name)


#Exercise 3: Area of a Room

#
#Ask user for width and length of room, then compute and display the area of the room and display with units (m).
#

width = float(input("Please enter the width of the room (in m's): "))
length = float(input("Please enter the length of the room (in m's): "))

area = width * length
print("The area of the room is", area, "square meters.")


#Exercise 4: Area of a Field

#
#Read length and width of farmer's field in feet and display area in acres.
#

width = float(input("Please enter the width of the field (in ft): "))
length = float(input("Please enter the length of the field (in ft): "))

acreage = (width * length) / 43560
print("The area of the field is", acreage, "acres.")


#Exercise 5: Bottle Deposits

#
#Read the number of containers of each size that a user deposits, calculate and display the refund with a $ to exactly 2 decimal places.
#

less = float(input("Please enter the # of 1L or less containers you're returning: "))
more = float(input("Please enter the # of 1L or more containers you're returning: "))

refund = (0.10 * less) + (0.25 * more)
print("The total refund for your containers is $", "{:.2f}".format(refund), ".")


# In[ ]:




