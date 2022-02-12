"""
Program: Simple Calculator 
Author: arif
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
import sys
result = 0 
num1 = 0
num2 = 0 


def num1():
       global num1 
       try:
              num1 = float(input("put your frist number : "))
              if num1 == isinstance(num1,float):
                     num1()
       except ValueError :
              print("is not a number put number agiat")
              num1()

def num2():
       global num2 
       try:
              num2 = float(input("put your second number"))
              if num2 == isinstance(num2,float):
                     num2()
       except ValueError :
              print("is not a number plase put the nomber againt")
              num2()


def operator(): 
       global result
       operation = input(
              """select the operation 
              + for addition 
              - for subtraction 
              * for multiplication 
              / for divition """)
       if (operation =='+' or operation == '-' or operation == '*' or operation == '/'):
              if operation == '+' :
                     addition()
              elif operation == '-' :
                     subtraction()
              elif operation == '*' :
                     multiplication()
              elif operation == '/' :
                     divition()
              else :
                     sys.exit("thanks you")
       else :
              print("invalid operation")
              operator()

def addition() :
       result = num1 + num2 
       print(f"your result equal to : {result} ")
       
def subtraction() :
       result = num1 - num2
       print(f"your result equal to : {result} ")
       
def multiplication() : 
       result = num1 * num2
       print(f"your result equal to : {result} ")
       
def divition() : 
       result = num1 / num2 
       print(f"your result equal to : {result} ")
       

def againt() : 
       loop = str(input("select Y for continud "))
       if loop.upper() == 'Y' : 
              num1()
              num2()
              operator()
       else : 
              sys.exit("thanks you")


num1()
num2()
operator()





       

