from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.color("blue")
colormode(255)
leo.color(99, 204, 250)

leo.begin_fill()
leo.end_fill()
done()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
done()

leo.speed(50)
leo.hideturtle()
done()

bob: Turtle = Turtle()

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1