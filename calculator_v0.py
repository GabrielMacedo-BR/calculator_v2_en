print('=========== CALCULATOR V 1.0 ============')


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operacao = input("Choose an operation (+, -, *, /): ")

if operacao == "+":
    resultado = number1 + number2
    print("Result:", resultado)

elif operacao == "-":
    resultado = number1 - number2
    print("Result:", resultado)

elif operacao == "*":
    resultado = number1 * number2
    print("Result:", resultado)

elif operacao == "/":
    if number2 != 0:
        resultado = number1 / number2
        print("Result:", resultado)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")