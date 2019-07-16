"""
Script to convert a sequence of number like strings to integer list
        ('1', '2', '3', '4') -> [1, 2, 3, 4]
"""
numbers_in_str = ('1', '2', '3', '4', '5', '6', '7')

# Apply int() function to all the elements in source list
integer_list = map(int, numbers_in_str)

print( list(integer_list) )    # [1, 2, 3, 4, 5, 6, 7] -> list of ints
