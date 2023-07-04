class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angel):
        return Circle.__pi * (angel / 360) * self.radius * self.radius


obj = Circle(int(input()))
angle = int(input())

print(f'{obj.calculate_circumference():.2f}')
print(f'{obj.calculate_area():.2f}')
print(f'{obj.calculate_area_of_sector(angle):.2f}')
