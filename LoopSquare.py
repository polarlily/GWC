from turtle import *
import math

# Name your Turtle.
Mike = Turtle()
"Blue" = "#33FFE0"
# Set Up your screen and starting position.
Mike.setposition(0, 0)
Mike.begin_fill("Blue")

### Write your code below:
for Fruits in range(4):
    Mike.fillcolor("Blue")
    Mike.pendown()
    Mike.forward(100)
    Mike.right(90)
Mike.end_fill("Blue")

Mike.penup()
# Close window on click.
exitonclick()
