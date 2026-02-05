print ('============ CALCULATOR V 2.1 ================')


def calculate(number1, number2, operation):
  if operation == '+':
    return number1 + number2
  elif operation == "-":
    return number1 - number2
  elif operation == '*':
    return number1 * number2
  elif operation =='/':
    if number2 == 0:
      return 'Cannot Divide by zero'
    return number1 / number2
  
  else: 
    return 'Invalid Operation'
  
number1 = float(input('Enter a number: '))
number2 = float(input('Enter another number: '))
operation = input('What is the arithmetic operation?: ').strip()

result = calculate(number1, number2 , operation)

print('Result: ',result)
