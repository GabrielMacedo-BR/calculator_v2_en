print ('========== Calculator V 2.1 ================')


def calculate(number1, number2, operation):
 if operation == '+':
  return number1 + number2
 elif operation == '-':
  return number1 - number2  
 elif operation == '*':
  return number1 * number2
 elif operation == '/':
  if number2 == 0:
   return 'Cannot Divide by Zero'
  return number1 / number2
 else:
  return 'Invalid Operation'
 
while True:
 try:
  number1 = float(input('Enter a number: '))
  number2 = float(input('Enter another number: '))
  operation = input('What is the arithmetic operation?:').strip().lower()

  result = calculate (number1, number2 , operation)

  print('Result: ',result)
  continue_calc = input('Continue? (y/n): ').lower()
  if continue_calc == 'n':
   break
  
 except ValueError:
  print('Invalid input. Please enter numbers only.')
  continue

