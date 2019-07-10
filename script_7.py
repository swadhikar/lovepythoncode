"""
    Explanation:
        In Python, we can override the behaviour of basic operators 
        with special methods in a class as below:

            +  (addition)        -   __add__
            -  (subtraction)     -   __sub__
            /  (division)        -   __div__
            *  (multiplication)  -   __mul__

        By doing so, we modify the behaviour of that operator itself
        For example, the "+" operator works on integers,

                        7 + 5 = 12

        Here, the integer objects 7 and 5 are added to return 12. When
        we can implement the __add__ special method with the self object
        and the other object (i.e. LHS and the RHS at the + operator) and
        change the behaviour. In the example below, we override the "+"
        operator to return add the Robot instances' memory attribute and
        return the summed memory.
"""
class Robot:
    """ Operator overloading example """
    def __init__(self, memory):
        self.memory = memory

    def __add__(self, other_robot_instance):
        """
            Overloads '+' operator to return sum of memory (self.memory)
            when operated on Robot instances
        """
        total_memory = self.memory + other_robot_instance.memory
        return total_memory

if __name__ == '__main__':
    robot_1 = Robot(100)
    robot_2 = Robot(200)


    total_robot_memory = robot_1 + robot_2
    print('Total robot memory:', total_robot_memory)  # Total robot memory: 300
