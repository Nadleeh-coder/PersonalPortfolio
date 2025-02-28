class Point:
    """
    Creates a Point given a set of coordinates and calculates the location
    within a rectangle.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


class Rectangle:
    """
    Creates a rectangle given a set of points and calculates its area.
    """
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GraphicalRectangle(Rectangle):
    """
    Object that represents a graphical representation of a rectangle inside a canvas.
    """
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GraphicalPoint(Point):
    """
    Object that represents a graphical representation of a Point inside a canvas.
    """
    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
