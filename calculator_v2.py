def show_header(): 
 print ('========== Calculator V 2.1 ================')

def add(a, b):
        return a + b
def subtract(a, b):
        return a - b
def multiply(a, b):
        return a * b
def divide(a, b):
   if b == 0:
      return 'Cannot Divide by Zero'
   return a / b

operations = {
   '+': add,
   '-': subtract,
   '*': multiply,
   '/': divide,
   '%': lambda a, b: a % b
}

def calculate(number1, number2, operation):
 function = operations[operation]
 return function(number1, number2)
  
def get_number(message):
   while True:
     try:
       number1 = float(input(message))
       return number1
     except ValueError:
       print('Invalid number, Try again')

def get_operation():
   while True:
     print('Available operation: + - * /')
     operation = input('What is the arithmetic operation?; ').strip().lower()
     if operation in ['+', '-', '*', '/']:
       return operation
     print('Invalid Operation, Try again!')

def should_continue():
  answer = input('Continue? (y/n): ').lower().strip()
  return answer != 'n'

show_header()

while True:
 number1 = get_number('Enter first number: ')
 operation = get_operation()
 number2 = get_number('Enter another number: ')

 result = calculate (number1, number2 , operation)
 print('Result: ', result)

 if not should_continue():
   break
 

