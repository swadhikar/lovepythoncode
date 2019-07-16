from random import randrange
class RandomNumberIterator():
    """ Random number iterator class """
    def __init__(self, count=10):
        self.count = count
    def __next__(self):
        while self.count > 0:
            self.count -= 1          # code to track state
            return randrange(0, 10)  # random no. between 0 and 10
        else:
            raise StopIteration      # Stop iteration explicitly
    def __iter__(self):
        return self

def random_number_generator(count=10):
    """ Random number generator """
    while count > 0:
        count -= 1
        yield randrange(0, 10)       # return the value and auto-track state

for num in RandomNumberIterator():   # Iterator method
    print(num, end=' ')              # 1 8 0 5 9 6 9 3 3 9

for num in random_number_generator():# Generator method
    print(num, end=' ')              # 9 0 4 1 4 2 6 0 6 2
