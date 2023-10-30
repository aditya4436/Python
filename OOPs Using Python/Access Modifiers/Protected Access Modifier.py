# Protected Access Specifier:- The members of a class that are declared
#                              protected are only accessible to a class
#                              derived from it. Data Members of a class
#                              are declared protected by adding a single
#                              underscore '_' symbol before the data member
#                              of that class.

class Details:
    # Below are the Protected Data Members.
    _name=None
    _age=None
    _branch=None
    
    def __init__(self, name, age, branch):
        self._name=name
        self._age=age
        self._branch=branch
        
    def Display(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Branch: {self._branch}")

class DerivedDetails:
    def __init__(self, name, age, branch):
        Details.__init__(self, name, age, branch)
    
    def DisplayDerivedDetails(self):
            print(f"Name: {self._name}")
        
obj=DerivedDetails("Aditya", 24, "CSE")

# Below is the code to display the details int the Derived Class.
obj.DisplayDerivedDetails()

# Below is the code to display the details in the Base Class.
obj1=Details("Aditya", 24, "CSE")
obj1.Display()