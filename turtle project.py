import turtle
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed("fastest")
pen.width(2)
pen.hideturtle()
def petal(size, outline, fill):
    pen.color(outline, fill)
    pen.begin_fill()
    for _ in range(2):
        pen.left(120)
        pen.circle(size, 60)
        pen.left(120)
        pen.circle(size, 60)
    pen.end_fill()
def star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)  # Point the star upward
    pen.color("yellow", "yellow")
    pen.pendown()
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()
colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet", "magenta", "pink"]
for i in range(36):
    color = colors[i % len(colors)]
    pen.setheading(i * 10)
    petal(70, "white", color)
pen.penup()
pen.goto(0, 0)
pen.pendown()
for i in range(72):
    pen.color(colors[i % len(colors)])
    pen.forward(120)
    pen.dot(10)
    pen.backward(120)
    pen.right(5)
star(-180, 0, 40)   
star(180, 0, 40)    
star(0, 180, 40)   
star(0, -180, 40)   
turtle.done()