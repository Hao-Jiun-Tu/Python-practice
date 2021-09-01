# HOW TO USE OBJECT
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX) ** 2 + (self.y-targetY) ** 2) ** 0.5

p = Point(3,4)
p.show()
result = p.distance(0,0) # distance from (3,4) to (0,0)
print(result)
