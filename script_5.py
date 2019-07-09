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

# Deprecated approach similar in other languages
is_matched = False  # An explicit flag to check if word exists

# Loop to traverse each element in the list
# and see if any of the names starts with 'J'
for word in word_list:
    if word.startswith('j'):
        is_matched == True

# Check for condition with another if statement
if is_matched:
    print('Match found!')
else:
    print('Match not found!')



# Pythonic approach to find item existence
for word in word_list:
    if word.startswith('j'):
        print('Found {} that starts with "j"!'.format(word))
        break       # break and exit from the "for-else" loop
else:
    # for loop is never been broken at this point
    print('Match not found!')

