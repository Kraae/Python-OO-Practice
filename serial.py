"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    
    >>> serial.generate()
    100
    

    >>> serial.generate()
    101


    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100


    """

    def __init__(self, start=100):
        """start at 100"""
        self.start = self.incr = start

    def __repr__(self):
        """
        returns a string representing the
        instance that can be used to recreate the object 
        in a way that it can be recreated
        """
        print(f"<SerialGenerator start={self.start} next={self.incr}>")

    def generate(self):
        """
        increase next increment by 1
        """
        self.incr += 1
        print(self.incr -1)

    def reset(self):
        """
        reset number to start again (100)

        """
        self.incr = self.start