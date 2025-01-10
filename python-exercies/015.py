class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

# Example usage
aCircle = Circle(3)
print(aCircle.area())