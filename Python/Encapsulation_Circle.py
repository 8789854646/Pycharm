class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def radius(self):
        print("Getting")
        return self._radius
    @radius.setter
    def radius(self, value):
        print("Setting")
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        self._radius = value
    def circumference(self):
        return 2*3.14*self._radius

c = Circle(4)

