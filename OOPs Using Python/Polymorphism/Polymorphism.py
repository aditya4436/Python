# Polymorphism:- The word polymorphism means having many forms. In 
#                programming polymorphism means the same function name
#                being used for different types. The key difference
#                is the data types and number of arguments used in the 
#                function.
class Bharat:
    def Capital(self):
        print("New Delhi is the capital of Bharat.")
    
    def Language(self):
        print("Hindi is the most widely spoken language in Bharat.")

class Russia:
    def Capital(self):
        print("Moscow is the capital of Russia.")
    
    def Language(self):
        print("Russian is the most widely spoken language in Russia.")

obj_Bharat=Bharat()
obj_Russia=Russia()
obj_Bharat.Capital()
obj_Bharat.Language()

obj_Russia.Capital()
obj_Russia.Language()