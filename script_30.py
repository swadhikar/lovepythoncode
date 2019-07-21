input_string = 'python'

# Usual way of creating a list with each character twice
result_list = []
for character in input_string:
    twice_the_char = 2 * character
    result_list.append(twice_the_char)

print( result_list )     # ['pp', 'yy', 'tt', 'hh', 'oo', 'nn']

# The comprehension way
result_list_2 = [ 2 * character for character in input_string]

print( result_list_2 )  # ['pp', 'yy', 'tt', 'hh', 'oo', 'nn']
