# Jose Ortiz
# 02-25-2021
# CIS112 - Spring 2021
# Assignment 3

if __name__ == "__main__":

    #Koopa Troopas
    import turtle
    redKoopa = turtle.Turtle()
    redKoopa.shape("turtle")
    redKoopa.color("red")
    redKoopa.hideturtle()
    greenKoopa = turtle.Turtle()  
    greenKoopa.shape("turtle")  
    greenKoopa.color("green")
    greenKoopa.hideturtle()
    blueKoopa = turtle.Turtle()
    blueKoopa.shape("turtle")
    blueKoopa.color("blue")
    blueKoopa.hideturtle()

    # Function definitions
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

    def Angles(sides):
        return 360 / sides
    
    def DrawShape(Koopa, sides, length):
        Koopa.showturtle()        
        for i in range(sides):
            Koopa.forward(length)
            Koopa.left(Angles(sides))
        Koopa.hideturtle()

    def SpinPolygon(Koopa, sides, angle, length, repeat):     
        redKoopa.clear()   
        Koopa.showturtle()        
        for i in range(repeat):
            for j in range(sides):
                Koopa.forward(length)
                Koopa.left(Angles(sides))
            Koopa.left(angle)
        Koopa.hideturtle()

    def ScalePolygon(Koopa, sides, length, sfactor, number):
        greenKoopa.clear()
        Koopa.showturtle()        
        for i in range(number):
            for j in range(sides):
                Koopa.forward(length)
                Koopa.left(Angles(sides))
            length *= sfactor
            Koopa.hideturtle()
    
    # Mainloop starts here
    sides = getSides()
    length = getLength()
    
    DrawShape(redKoopa, sides, length)
    SpinPolygon(greenKoopa, sides, getAngle(), length, getRepeat())
    ScalePolygon(blueKoopa, sides, length, getScale(), getNumber())

    print("\n\nSafe to Close Graphic Window to Proceed...")
    turtle.done()
    # End Mainloop
    