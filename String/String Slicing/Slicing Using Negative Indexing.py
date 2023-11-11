# Slicing Using Negative Indexes:- When we use negative index, the python interpretates
#                                  it as "len(string) - the given negative index".
#                                  Example:- string[len(string)-4 : len(string)-1]
string="Aditya"
print(f"{string[-4:-1]}")