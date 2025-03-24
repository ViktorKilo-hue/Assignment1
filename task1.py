#Perform Basic Mathematical Operations

#Function to print mathematical operations
def calculator(num1, num2):
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2:.2f}")
    try:
        print(f"Division: {num1 / num2:.2f}")
    #Exception to handle Division by Zero    
    except ZeroDivisionError:
        print("Error! Cannot divide by zero!")


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
#Exception to handle Value based Errors
except ValueError:
    print("Invalid input!")
else:
    calculator(num1,num2)
