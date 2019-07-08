
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