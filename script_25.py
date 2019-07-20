import time

class WaitBeforeExecute:
    def __init__(self, function):
        self._function = function

    def __call__(self, message):
        time.sleep(1)               # pause for a second
        self._function(message)

@WaitBeforeExecute
def print_this(message):
    print(message + ' printed post wait')


print_this('random text')          # random text printed post wait
