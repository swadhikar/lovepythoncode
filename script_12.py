"""
    Multiple imports from a single module such as classes or functions
    can be multilined similar to the way we define a tuple object. This
    makes the import look so elegant and prevents a lengthy long ugly lines
    of code
"""
from time import (
    sleep,
    ctime,
    localtime,
    time
)


print(dir()) # ['ctime', 'localtime', 'sleep', 'time', ...]
