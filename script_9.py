class StringNotAllowedException(Exception):  # inherit from Exception class
    """ Custom exception to represent string is disallowed """
    pass


""" Program to calculate square root of numbers """
unclean_list = [7, 'eight', 9, 'ten']    # A random list

for num in unclean_list:
    try:
        if type(num) is str:
            raise StringNotAllowedException  # raise exception intentionally

        square_root = num ** 0.5
        print('square root of "{}": {}'.format(num, square_root

    except StringNotAllowedException as e:
        print('<<<Invalid number: {}>>>'.format(num))  # handle exception
