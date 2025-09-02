import turtle
# Setup Screen

screen = turtle.Screen()
screen.bgcolor("lightpink")
screen.title("Turtle Basics - All in One")

# Create a turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(2)


# Movement Basics
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.backward(100)
pen.right(90)
pen.forward(190)

# Pause before next section
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Square
pen.color("red")
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Pause before next section
pen.penup()
pen.goto(190, 0)
pen.pendown()

# Circle
pen.color("green")
pen.circle(60)

# Pause before next section
pen.penup()
pen.goto(0, -150)
pen.pendown()

# Star
pen.color("purple")
for _ in range(5):
    pen.forward(100)
    pen.right(144)

# Pause before next section
pen.penup()
pen.goto(-50, 150)
pen.pendown()

# Writing Text
pen.color("black")
pen.write("Thanks for watching my Turtle !!", font=("Times new roman", 14, "italic"))

# Hide Turtle & Keep Window Open
pen.hideturtle()
screen.mainloop()
