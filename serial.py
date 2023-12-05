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
    run_count = 0
    def __init__(self, start):
        self.start = start

    def generate(self):
        self.run_count +=1
        return self.start + self.run_count - 1
    
    def reset(self):
        self.run_count = 0