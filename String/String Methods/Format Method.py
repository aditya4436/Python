# format():- This method formats the specified value(s) and insert them
#            inside the string's placeholder. The placeholder is defined
#            by using curly brackets: {}.
string="For only {percentage:.2f} rupees."
print(string.format(percentage = 78))