import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Set up the first turtle (tess)
tess = turtle.Turtle()
tess.pensize(5)
tess.color("blue")

# Set up the second turtle (alex)
alex = turtle.Turtle()
alex.color("black")

# Function for tess to draw a square
def draw_square(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)

# Function for alex to draw a star
def draw_star(t):
    for _ in range(5):
        t.forward(150)
        t.right(144)

# Move tess to a different starting position
tess.penup()
tess.goto(-200, 0)
tess.pendown()

# Move alex to a different starting position
alex.penup()
alex.goto(200, 0)
alex.pendown()

# Draw shapes
draw_square(tess)
draw_star(alex)

# Keep the window open until it is closed by the user
wn.mainloop()
