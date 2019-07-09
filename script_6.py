"""
    A brief note on set:
        - Sets are unordered sequence of data
        - They do not allow duplicate values
    Note that set declaration consists of curly braces without the ':' symbol
"""
# A simple set
name_set = {'sai', 'sri', 'sai', 'ram', 'ram', 'sri'}
print(name_set)    # {'sri', 'sai', 'ram'}

# Incorrect way to create an empty set
empty_set = {}
print(type(empty_set))      # <class 'dict'> !?

# How to go about creating an empty set?
empty_set = set()
print(type(empty_set))      # <class 'set'>


"""
Explanation:

    Unlike list or dict, creating an empty set cannot be done by open closing
    a paranthesis sytax. For example,

        empty_list = []
        empty_dict = {}

    Apparently from the above code,

        empty_set = {}

    resulted in a dictionary with no items. In Python, sets can only be
    created with the builtin "set()"function similar to list() or dict().
    This is the only way you can create a set with no items.
"""
