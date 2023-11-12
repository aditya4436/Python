def PrintNumber(num1, num2=20):
    # If we don't pass any number for "num2" then the default number
    # will be printed "20".
    print(f"The first number is taken as input from the user {num1}.")
    print(f"The second number is a default number {num2}.")

number1=int(input("Enter a number: "))
PrintNumber(number1, 11)
# If we don't pass "11" then the default number i.e., 20 will be printed.