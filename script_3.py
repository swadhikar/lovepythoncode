
print("Approach 1: Store the first item in a sequence into a variable")

my_local_ip, *other_ips = ['127.0.0.1', '10.197.75.53', '10.197.75.54', '10.197.75.55']

print(my_local_ip)              # 127.0.0.1
print(other_ips, end='\n\n')    # list: ['10.197.75.53', '10.197.75.54', '10.197.75.55']
"""
    Explanation:
    
        The syntax *variable indicates that the variable matches the rest of the sequence
        (list, tuple or any iterable) as a list
"""

print("Approach 2: Suppose you want the second item in a sequence to be stored")

_, my_local_ip, *_ = ['10.197.75.53', '127.0.0.1', '10.197.75.54', '10.197.75.55']
print(my_local_ip, end='\n\n')  # 127.0.0.1
"""
    Explanation:

    *_  
        In python a single underscore is used to suppress a value. For example,
        
        _, lastname = ("swadhikar", "chandramohan")
        
        indicates that we are interested in last name only and would like to ignore
        the first item in the assignment. In such cases, we normally use _ to suppress
        one value and *_ to suppress a group of items in a sequential manner
"""

print("Approach 3: Suppose you want the to store the first and last item in a variable")

list_of_ips = ['127.0.0.1', '10.197.75.53', '10.197.75.54', '10.197.75.55', 'localhost']
my_local_ip_1, *_, my_local_ip_2 = list_of_ips
print(my_local_ip_1)            # 127.0.0.1
print(my_local_ip_2)            # localhost


"""
    var_1, *_, var2 = ['list', 'of', 'values', 'to', 'select', 'from']
    
    This indicates the we are interested in the first and list elements in the 
    sequence assingnment. Hence, we suppress all the intermediate elements in the list
"""