# CNE330 Network Programming in Python
# Adam Hooker-Brown
# Nov 20th 2024

# This is my calculator for the final project!

# importing math for log & factorial
import math

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ C A L C U L A T O R ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# while 1 creates loop for calculator so it doesn't end after one operation
while 1:

# introduces user to the features that the calculator has
    print("\nWhat type of calculation would you like to do? (Type the number and press enter to continue)")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Factorial")
    print("8. Exit")

#asks for user input to choose feature
    user_choice = int(input("Enter your number choice: "))

# asks for 2 numbers and prints the sum
    if user_choice == 1:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("\nAddition answer:", num1 + num2)

# asks for 2 numbers and prints the difference
    elif user_choice == 2:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("\nSubtraction answer:", num1 - num2)

# asks for two numbers and prints the product
    elif user_choice == 3:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("\nMultiplication answer:", num1 * num2)

# asks for two numbers and prints the quotient
    elif user_choice == 4:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("\nDivision answer:", num1 / num2)

# asks for two numbers calculates exponentiation
    elif user_choice == 5:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print("\nExponentiation answer:", num1 ** num2)

#asks for a single number and calculates the logarithm using math.log (base 10)
    elif user_choice == 6:
        num1 = float(input("Enter your number: "))
        print("\nLogarithm answer:", math.log10(num1))

#asks for a whole number and calculates the factorial
    elif user_choice == 7:
        num1 = int(input("Enter your whole number: "))
        print("\nFactorial answer:", math.factorial(num1))

#exits the program using break if user types 8 in beginning menu
    elif user_choice == 8:
        print("Exiting... Goodbye!")
        break

#Sources:
#https://www.geeksforgeeks.org/
#Used GeeksForGeeks for method on logarithms, factorials, & break
