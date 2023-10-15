import math

print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Cube Root")

choice = input("Enter choice (1-7): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
elif choice in ['6', '7']:
    num = int(input("Enter a number: "))

if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error! Division by zero.")
elif choice == '5':
    result = num1 ** num2
    print("Result: ", result)
elif choice == '6':
    if num >= 0:
        result = math.sqrt(num)
        print("Result: ", result)
    else:
        print("Error! Invalid input for square root.")
elif choice == '7':
    if num >= 0:
        result = num ** (1/3)
        print("Result: ", result)
    else:
        print("Error! Invalid input for cube root.")

else:
    print("Invalid choice. Please enter a number between 1 and 7.")
