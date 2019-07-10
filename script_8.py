print( bool(None) )      # False
print( bool(0) )         # False
print( bool(1) )         # True (for any non zero integer)

class House:
    """ bool() function demo class """
    def __init__(self, rooms_count, gardens_count=None):
        self.rooms_count = rooms_count
        self.gardens_count = gardens_count

    @property
    def has_garden(self):
        """
            The bool() function eliminates 2 lines of code below:
                if len(self.gardens_count) == 0:
                    return False
        """
        return bool(self.gardens_count)    # bool(0 or None) -> False

house_1 = House(3, 2)
print( house_1.has_garden )    # True

house_2 = House(2)               # default arg, gardens_count=None
print( house_2.has_garden )    # False

house_3 = House(2, 0)
print( house_3.has_garden )    # False
