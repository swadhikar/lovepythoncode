""" Script that prints strings as csv (comma separated values) """

COMMA = ','
string = 'lovepythoncode'

# Method 1: Using "end" keyword argument of print function (Nearly CSV)
print("Method 1: print() function with end param (extra , at the end)")
for char in string:
    print(char, end=COMMA)

# Method 2: Using string's join() method
str_as_csv = ','.join(string)

print('\n\nMethod 2: Using string.join() method (perfect csv)')
print(str_as_csv)
