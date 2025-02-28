import turtle
from random import randint
from geometry import Point, GraphicalPoint, GraphicalRectangle

rectangle = GraphicalRectangle(
    Point(
        randint(0, 200),
        randint(0, 200)
    ),
    Point(
        randint(201, 400),
        randint(201, 400)
    )
)

print(f"Rectangle Coordinates: {rectangle.point1.x}, {rectangle.point1.y} "
      f"and {rectangle.point2.x}, {rectangle.point2.y}")

user_point = GraphicalPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print(f"Your point was inside the rectangle: {user_point.falls_in_rectangle(rectangle)}")
print(f"Your area was off by: {rectangle.area() - user_area}")

my_turtle = turtle.Turtle()
rectangle.draw(my_turtle)
user_point.draw(my_turtle)
turtle.done()
