emp_dict = { 'hcl': 1000, 'tcs': 1500, 'cts': 650 }

# Usual sorting
sorted_list = sorted(emp_dict)   # sorts company names in alphabetical order
print(sorted_list) # ['cts', 'hcl', 'tcs']

"""
The sorted function should operate on dict.items(): [(a, b), (c, d), ...]
Modify it's "key" argument with the lambda function

    key = lambda x: x[1] # The lambda function should fetch the second item
"""

# Sorted by ascending order of the values
sorted_list = sorted(emp_dict.items(), key=lambda x: x[1])
print(sorted_list) # [('cts', 650), ('hcl', 1000), ('tcs', 1500)]

# Sorted by descending order of the values
sorted_list = sorted(emp_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_list) # [('tcs', 1500), ('hcl', 1000), ('cts', 650)]
