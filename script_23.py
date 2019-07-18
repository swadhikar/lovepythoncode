<<<<<<< HEAD
class MyClass:
    def __init__(self):
        """Object constructor"""
        pass

    def test_method(self, arg_1, arg_2):
        """
            A simple test method that does nothing
            @param   arg_1 (string)   simple argument
            @param   arg_2 (int)      another argument
        """
        pass

print( help(MyClass) )

# class MyClass(builtins.object)
#  |  This is a demo class that shows the use of docstrings!
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self)
#  |      Object constructor
#  |
#  |  test_method(self, arg_1, arg_2)
#  |      A simple test method that does nothing
#  |      @param   arg_1 (string)   simple argument
#  |      @param   arg_2 (int)      another argument
#  |

def is_palindrome(string):
    return string[::-1] == string


is_palindrome('amma')     # True
is_palindrome('hello')    # False
