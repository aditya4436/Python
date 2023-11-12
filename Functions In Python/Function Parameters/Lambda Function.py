# Lambda Function:- In Python, an anonymous function means that a function
#                   without name. As we already know the 'def' keyword is used
#                   to define the normal functions and lambda keyword is used
#                   to create anonymous functions. It is better to use lambda 
#                   function when the function definition is not huge.
cube=lambda x: x*x*x

number=int(input("Enter the number: "))
print(f"The cube of the given number is: {cube(number)}")