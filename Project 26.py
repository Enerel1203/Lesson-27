class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

a = float(input("Enter the radius: "))

b = Circle(a)

print("Area of circle:", b.area())
print("Perimeter of circle:", b.perimeter())