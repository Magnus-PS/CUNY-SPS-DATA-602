#!/usr/bin/env python
# coding: utf-8

# In[11]:


#These exercises were derived from Ben Stephenson's 'The Python Workbook'

#The aim of using this text is to refine my own Python programming capabilities via:
##(1) completing the exercises therein, and
##(2) comparing solutions with those provided by the author


#--->Section: Intro to Programming<---#

#Exercise 27: BMI

#
#Write a program that computes the body mass index (BMI) of an individual. 
#

#Read the height and weight from the user.
height = float(input("Please enter your height (in inches): "))
weight = float(input("Please enter your weight (in lbs): "))

#Compute the BMI
BMI = (weight / height**2) * 703

#Display the BMI
print("Your BMI is ", BMI, ".")

#Extra credit: print out whether or not they're obese (BMI >= 30)
if (int(BMI) >= 30):
    print("You're obese.")
else:
    print("You're not obese.")


#Exercise 29: Celsius to Farenheit and Kelvin

#
#Read a temperature (in Celsius) from the user and convert to Farenheit and Kelvin.
#

#Read a temperature from the user
C_temp = float(input("Please enter a temperature (in Celsius): "))

#Convert the temperature to Farenheit

F_temp = (C_temp * (9/5)) + 32

#Convert the temperature to Celsius

K_temp = C_temp + 273

#Display the converted temperatures
print(C_temp, "Celsius is", F_temp, "Farenheit and ", K_temp, "Kelvin.")


#Exercise 31: Sum of Digits in an Integer

#
#Read a four-digit integer from the user and display the sum of the digits in the number.
#

#Read four-digit integer from the user
four_dig = input("Please enter a four-digit integer: ")
dig_1 = int(four_dig[0])
dig_2 = int(four_dig[1])
dig_3 = int(four_dig[2])
dig_4 = int(four_dig[3])

dig_sum = dig_1 + dig_2 + dig_3 + dig_4

print("The sum of the digits is:", dig_sum)


# In[ ]:




