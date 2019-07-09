"""
Explanation:

The for-else loop which is usually a for-break-else loop is more handy
when you want to traverse through a list and check for a conditional using
if statement without using a separate flag variable. In most other
programming languages, a flag variable is essential to check for a
condition and another if-else to carry out processing. Consider the below
codes, they are technically equal but far simpler and readable in python.
"""


word_list = ['Mary', 'had', 'a', 'little', 'lamb']
search_word = 'John'


# Deprecated approach similar in other languages
is_word_found = False  # An explicit flag to check if word exists

# Loop to traverse each element in the list
for word in word_list:
    if word == search_word:
        is_word_found == True

# Check for item existance
if is_word_found:
    print('Found {}!'.format(search_word))
else:
    print('{} is not found!'.format(search_word))



# Pythonic approach to find item existence
for word in word_list:
    if word == search_word:
        print('Found {}!'.format(search_word))
        break       # break and exit from the "for-else" loop
else:
    # for loop is never been broken
    print('{} is not found!'.format(search_word))

