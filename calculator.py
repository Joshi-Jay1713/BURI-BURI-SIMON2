import math





print("****** SIMPLE NUMBERS CALCULATOR ******\n\n")
print("""Choose an operation:
1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division""")

next_operation = "yes"

while next_operation.lower() == "yes":
    # Get operation input
    operation = input("Type the number for the operation you want: ")
    
    if operation in ["1", "2", "3", "4"]:
        try:
            # Get numbers as input
            num1 = float(input("Type your first number: "))
            num2 = float(input("Type your second number: "))
            
            # Perform the selected operation
            if operation == "1":
                ans = num1 + num2
                print(f"Your answer is: {ans}")
            elif operation == "2":
                ans = num1 - num2
                print(f"Your answer is: {ans}")
            elif operation == "3":
                ans = num1 * num2
                print(f"Your answer is: {ans}")
            elif operation == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    ans = num1 / num2
                    print(f"Your answer is: {ans}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid operation. Please choose a valid option.")
    
    # Ask if the user wants to continue
    next_operation = input("Do you want to continue? Type 'Yes' or 'No': ").strip()

print("Thank you for using the calculator. Goodbye!")