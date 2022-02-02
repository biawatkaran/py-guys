class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def move():
        print("move")

    @staticmethod
    def draw():
        print("draw")


point1 = Point(10, 20)
print(point1.x, point1.y)
point1.draw()
