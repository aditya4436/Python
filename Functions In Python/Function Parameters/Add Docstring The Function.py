# Doctstring:- The first string after the function is called the Document String
#              or Doctstring in short. This is used to describe the functionality
#              of the function. The use of docstring in function is optional but
#              it is considered a good practice. Docstring is denoted by triple
#              inverted commas.
def SquareOfANumber(num: int):
    """This is a docstring and this function squares up the given number."""
    square=num*num
    print(f"The square of a given number is {square}.")

print(SquareOfANumber.__doc__)
# The above print function prints the docstring inside the function is printed.
number=int(input("Enter a number: "))
SquareOfANumber(number)