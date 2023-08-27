#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      vyenk
#
# Created:     26-08-2023
# Copyright:   (c) vyenk 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Mini Project  ("Based on Calculator")

first = input(" Enter your first number : ")

second = input(" Enter your second number : ")

operator = input(" Enter your operator(+ , - , *, /, %) : ")

first = int(first)
second = int(second)

if operator == "+" :
    print(first + second)

elif operator == "-" :
    print(first - second)

elif operator == "*" :
    print(first * second)

elif operator == "/" :
    print(first / second)

elif operator == "%" :
    print(first % second)

else :
    print(" This is an invalid operation ")