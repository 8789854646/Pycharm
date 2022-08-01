class Book:
    def __init__(self, pages):
        self.pages = pages
    def __str__(self):
        return 'The number of pages:'+str(self.pages)
    def __add__(self, other):
        total = self.pages + other.pages
        b = Book(total)
        return b
    def __mul__(self, other):
        total = self.pages * other.pages
        b = Book(total)
        return b
    def __divmod__(self, other):
        total = self.pages / other.pages
        b = Book(total)
        return b

b1 = Book(200)
b2 = Book(300)
b3 = Book(600)

print(b1+b2)
print(b1+b2+b3)