import turtle

userLength = int(input("Enter length of sides: "))

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

# window closes when clicked on, or permanently stays open if input() function is used instead
turtle.exitonclick()
