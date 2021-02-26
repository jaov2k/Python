# Jose Ortiz
# 02-25-2021
# CIS112 - Spring 2021
# Assignment 2 
#
# PURPOSE:
#       Creates 6 concentric squares on center, taking advantage of the 'Turtle' module
# PARAMETERS:
#       None
# RETURN VALUES:
#       None
# FUNCTION SINGATURE:
#       None

if __name__ == "__main__":
    import turtle
    turtle.penup()
        
    # Starting coordinates and values
    side = 120
    shrink = 10
    x = -60
    y = 60   

    while side > 0:
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        side -= shrink * 2
        x += shrink
        y -= shrink
        turtle.penup()        
    turtle.done()