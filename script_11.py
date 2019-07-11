""" Script that changes print() function to log timestamp before printing the message """

from builtins import print as print_    # lets rename and import print builtin
from time import ctime, sleep


def print(message):
    """ Overridden print function that logs timestamp first """
    print_(ctime(), ':', message)


print('log line 1')   # Renovated print function that logs timestamp at the start
sleep(3)
print('log line 2')
sleep(3)
print('log line 3')


""" Result """
# Thu Jul 11 16:24:26 2019 : log line 1
# Thu Jul 11 16:24:29 2019 : log line 2
# Thu Jul 11 16:24:32 2019 : log line 3
