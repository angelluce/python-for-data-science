class Circle():
    def __init__(self, rad, col) -> None:
        self.rad = rad
        self.col = col
    
    def add_radius(self, rad) -> None:
        self.rad = self.rad + rad

print("Answer 1: ", len(["a"]))

circle = Circle(3, "blue")

print("Answer 2: ", circle.col)

circle.rad = 1

print("Answer 3: ", circle.rad)

circle.add_radius(20)

print("Answer 4: ", circle.rad)
