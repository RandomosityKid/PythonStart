class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
print(rectangle.area)  # Output: 50
rectangle.width = 7
print(rectangle.area)  # Output: 70