class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    @property
    def length(self):
        print("Getting length")
        return self._length
    @property
    def breadth(self):
        print("Getting breadth")
        return self._breadth
    @length.setter
    def length(self, value):
        print("Setting length")
        if not isinstance(value,(int, float)):
            raise Exception("Only numbers are allowed")
        self._length = value
    @breadth.setter
    def breadth(self, value):
        print("Setting Breadth")
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        self._breadth = value
    def perimeter(self):
        return 2*(self._length+self._breadth)

r = Rectangle(5,8)