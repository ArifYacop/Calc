"""
Program: Simple Calculator 
Author: Anas Tawalbeh
Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

number1=int(input("Insert the first value"))
number2=int(input("Insert the second value"))


operater = str(input("Select operations form +, -, *, / :"))
if isinstance (number1,int)== True and isinstance(number2,int)== True :
   addition=number1+number2
   subtraction=number1-number2
   multiplication=number1*number2
   division=number1/number2
else : 
   print("you must to enter number ")


if operater == "+" :
       print(f"The addition for the two values is equal to: {addition}")

elif operater ==  "-" :
       print(f"The subraction for the two values is equal to: {subtraction}")

elif operater == "*" :
       print(f"The multiplication for the two values is equal to: {multiplication}")

elif operater == "/" :
       print(f"The division for the two values is equal to: {division}")
else:
        print("invalid input")