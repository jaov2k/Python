# Jose Ortiz
# 02-25-2021
# CIS112 - Spring 2021
# Assignment 3
# PURPOSE:  Using the Turtle module, create a series of polygons
#           utilizing loops and passing values between the functions.
#           Made variable names obvious to their local scope to emphasize
#           them being passed between the functions.

#Koopa Troopas
import turtle

# Function Definitions
def getSides():
    return int(input("Please enter the number of sides of the polygon: "))    
def getLength():
    return int(input("Please enter the length of sides of the polygon: "))
def getScale():
    return int(input("Please enter the scale factor of the polygon: "))
def getAngle():
    return int(input("Please enter the angle of rotation: "))
def getRepeat():
    return int(input("Please enter the number of repetitions: "))
def getNumber():
    return int(input("Please enter the number of copies: "))

def Angles(angleSides):
    return 360 / angleSides

def DrawShape(drawKoopa, drawSides, drawLength):
    for i in range(drawSides):
        drawKoopa.forward(drawLength)
        drawKoopa.left(Angles(drawSides))
    return drawSides, drawLength, drawKoopa    

def SpinPolygon(spinKoopa, spinSides, spinAngle, spinLength, spinRepeat):
    spinKoopa.clear() 
    for i in range(spinRepeat):
        DrawShape(spinKoopa, spinSides, spinLength)
        spinKoopa.left(spinAngle)
    return spinKoopa  
    
def ScalePolygon(scaleKoopa, scaleSides, scaleLength, scaleSfactor, scaleNumber): 
    scaleKoopa.clear()     
    for i in range(scaleNumber):
        DrawShape(scaleKoopa, scaleSides, scaleLength)
        scaleLength *= scaleSfactor
    
# Mainloop starts here
if __name__ == "__main__":
    mainKoopa = turtle.Turtle()
    mainKoopa.shape("turtle")

    mainKoopa.color("red")        
    mainSides, mainLength, mainKoopa = DrawShape(mainKoopa, getSides(), getLength())
    mainKoopa.color("green")
    mainKoopa = SpinPolygon(mainKoopa, mainSides, getAngle(), mainLength, getRepeat())
    mainKoopa.color("blue")
    ScalePolygon(mainKoopa, mainSides, mainLength, getScale(), getNumber())

    print("\n\nSafe to Close Python Turtle Graphics Window to Proceed...")
    turtle.done()
# End Mainloop
    