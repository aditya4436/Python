# Access Specifiers:- Python uses '_'(underscore symbol) to determine the access control
#                     of the data member or a member function of a class. Access Specifiers
#                     in Python have important role to play in securing the data from
#                     unauthorized access and preventing it from being exploited.

# A class in Python has three access specifiers or modifiers:-
# (1):- Public Access Modifier
# (2):- Private Access Modifier
# (3):- Protected Access Modifier

# (1):- Public Access Modifier:- The member of a class that are declared public are easily
#                                accessible from any part of the program. All data members
#                                and functions of a class are public by default.
class Number:
    def __init__(self):
        self.number=1
    
    def showNumber(self):
        print(f"The number is {self.number}")

obj=Number()
obj.showNumber()