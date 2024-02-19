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

    def __init__(self,start):
        """Initializes serial number generator from start int."""
        if not isinstance(start,int):
            raise ValueError("Not a valid integer!")
        self.start = self.next = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start}"

    def generate(self):
        """Returns the next sequential number each time a new number is asked for.
        Will always generate start attribute as the very first return of method."""
        self.next += 1
        return self.next - 1
        
    def reset(self):
        """Resets the serial generator as if generate method was never called."""
        self.next = self.start

