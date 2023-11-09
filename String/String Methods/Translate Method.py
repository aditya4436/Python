# translate():- It returns a string where some specified characters are
#               replaced with the character described in a dictionary, or
#               in a mapping table.
dictionary={68: 66}
# 68 is the ascii value of "D" and 66 is ascii value of "B".
# Therefore the character "D" will be replaced with character "B".
string="Hello Dear"
print(f"{string.translate(dictionary)}")