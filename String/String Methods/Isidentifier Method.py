# isidentifier():- Returns True if the string is a valid identifier, otherwise
#                  False.
# A string is considered to a valid identifier it it only contains alphanumeric
# letters (a-z) and (0-9) or underscores (_). A valid identifier cannot start
# with a number or any spaces.
string1="Aditya"
string2="Aditya123"
string3="123Aditya"
string4="Aditya Kumar"
print(string1.isidentifier())
print(string2.isidentifier())
print(string3.isidentifier())
print(string4.isidentifier())