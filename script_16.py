""" The exec(string) function takes a string and runs as if interpreter
does the execution. For example, the below line:

    exec('name = "John Doe"')   # exec(string)
    print(name)                 # John Doe

In similar fashion, we can evaluate dataypes such as dict, list etc.
This is imperative while parsing python datatypes from a text like
config file without using external libraries such as astlib and so on.
"""
# String that looks like dictionary
dict_as_str = '''{
    'a': 'alphabet',
      1: 'integer',
   'pi': 3.14
}'''

# String that looks like list
list_as_str = '["oppo", "samsung", "apple", "vivo", "xiomi"]'

exec('dict_from_str = ' + dict_as_str)  # evaluates result to variables
exec('list_from_str = ' + list_as_str)  # dict_from_str and list_from_str

print(dict_from_str)    # {'a': 'alphabet', 'pi': 3.14, 1: 'integer'}
print(list_from_str)    # ['oppo', 'samsung', 'apple', 'vivo', 'xiomi']
