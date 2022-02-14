"""EX04 - Turtle Scene of Various Shapes. Part 8: I tried drawing a hexagon."""

__author__ = "730414608"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entry point of my scene."""
    leo: Turtle = Turtle()
    draw_square(leo, 0, 0)
    draw_square(leo, -200, 90)
    draw_triangle(leo, -200, -200)
    draw_rectangle(leo, 150, -50)
    draw_hexagon(leo, -250, -50)
    done()


def draw_square(turtle: Turtle, x: float, y: float) -> None:
    """Draw a square whose bottom left corner is at (0, 0)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    i: int = 0
    while (i < 4):
        turtle.forward(300)
        turtle.left(90)
        i += 1
    turtle.penup()
    turtle.goto(5, 5)
    turtle.setheading(0.0)


def draw_triangle(turtle: Turtle, x: float, y: float) -> None:
    """Draw a triangle bottom left corner is at (-200, 200)."""
    colormode(255)
    turtle.color(99, 204, 250)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    i: int = 0
    while (i < 3):
        turtle.forward(300)
        turtle.left(120)
        i = i + 1
    turtle.end_fill()


def draw_rectangle(turtle: Turtle, x: float, y: float) -> None:
    """Draw a rectangle bottom left corner is at (150, -50)."""
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()

    side_length: int = 125
    i: int = 0
    while (i < 2):
        turtle.forward(side_length)
        turtle.right(90)
        turtle.forward(side_length + side_length)
        turtle.right(90)
        i += 1


def draw_hexagon(turtle: Turtle, x: float, y: float) -> None:
    """Draw a hexagon bottom left corner is at (-250, -50)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    i: int = 0
    while (i < 6):
        turtle.forward(120)
        turtle.left(60)
        i += 1


if __name__ == "__main__":
    main()