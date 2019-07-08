
large_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print('Naive approach of looping a list with a extraneous variable, "index"')

index = 1   # A pivotal value to indicate the index

for alphabet in large_list:
    print('{}. {}'.format(index, alphabet))
    index = index + 1    # increment index by 1



print('\nPythonic approach using "enumerate()" function')

for index, alphabet in enumerate(large_list, start=1):
    print('{}. {}'.format(index, alphabet))

"""
The enumerate(list) function takes in a list or tuple and returns
a list of tuples with the auto manipulated index as the first element of 
tuple and the second element with the iterated value. For example,

enumerate(['a', 'b', 'c']) would return [(0, 'a'), (1, 'b'), (2, 'c')]

where the index by default is 0. we need to set the start keyword argument
equal to 1 to want indexes from 1, 2, 3 and so on. 

"""