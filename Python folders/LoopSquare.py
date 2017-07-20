from turtle import *
import math

# Name your Turtle.
Mike = Turtle()

# Set Up your screen and starting position.
Mike.setposition(0, 0)

### Write your code below:
for Fruits in range(4):
    Mike.pendown()
    Mike.forward(100)
    Mike.right(90)
Mike.penup()
# Close window on click.
exitonclick()
