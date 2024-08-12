import turtle

ws = turtle.Screen() # starting the screen
ws.bgcolor("lightblue")

# Set up the turtle (levi)
levi = turtle.Turtle()
levi.pensize(2)
levi.color("red")

side_length = 200  
levi.penup()  
levi.goto(-side_length / 2, side_length / 2) 
levi.pendown()  
for _ in range(4):
    levi.forward(side_length)
    levi.right(90)

levi.penup()
levi.goto(0, 0)  # Move to the center of the square
levi.pendown()

for _ in range(36):
    levi.forward(100)
    levi.right(170)

ws.mainloop()
