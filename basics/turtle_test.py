import turtle # import turtle library

wn = turtle.Screen()  # Create a graphic window, Use Screen with a capital 'S'
alex = turtle.Turtle() #create a turtle named 'alex'

alex.forward(150) # tell alex to move forward by 150 units

alex.left(90) # turn left by 90 degrees
# Keep the window open until it is closed by the user
wn.mainloop()
