import turtle

userLength = int(input("Enter length of sides: "))

turtle.pencolor('turquoise')
turtle.width(10)
turtle.speed(2)
turtle.fillcolor('pink')

def drawSide(userLength):
    turtle.forward(userLength)
    turtle.right(90)
    return 

def drawSquare(userLength):
    for i in range(4):
        drawSide(userLength)
    return userLength * userLength

area = drawSquare(userLength)
print ("The area of the square is " + str(area) + "!")

turtle.exitonclick()
