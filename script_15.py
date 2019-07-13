

windows_path = 'c:\\Users\\username\\filename.txt'

# The above path consists of backslash \ escaped by \ again
# is processed by python interpreter to convert to single \

print(windows_path)  # c:\Users\username\filename.txt


"""
    Sometimes its confusing when to use backslashes while working
    with windows paths. In those cases, we can consider using
    raw string which instructs python not to process the given
    string. For example, not to convert escaped characters like
    \\ to \
"""

windows_path = r'c:\Users\username\filename.txt'

print(windows_path) # c:\Users\username\filename.txt
