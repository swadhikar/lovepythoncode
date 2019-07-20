def get_shifted_string(s, offset_left, offset_right):
    """Function that shifts characters in a string by given offsets"""
    s = s[offset_left: ] + s[:offset_left]     # shift left  by 2: cdab
    s = s[-offset_right:] + s[:-offset_right]  # shift right by 1: bcda
    return s


s = get_shifted_string('abcd', offset_left=2, offset_right=1)
print(s)    # bcda
