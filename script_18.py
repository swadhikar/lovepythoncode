"""
    Write a dictionary comprehension to create a dictionary with below values:

    {'0-1': 0, '2-3': 0, '4-5': 0, '6-7': 0, '8-9': 0}

    (order need not be preserved)
"""
# Regular approach
result_dict = dict()
value = 0

for num in range(0, 10, 2):
    key = '{}-{}'.format(num, num + 1)
    result_dict[key] = value
print(result_dict)   # {'0-1': 0, '6-7': 0, '4-5': 0, '8-9': 0, '2-3': 0}

# comprehensive way
result_dict = {
    '{}-{}'.format(num, num + 1): value
    for num in range(0, 10, 2)
}
print(result_dict)   # {'8-9': 0, '2-3': 0, '6-7': 0, '4-5': 0, '0-1': 0}
