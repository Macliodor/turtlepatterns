import turtle
from random import choice

def generateHexColor():
    return "#" + "".join(choice("0123456789ABCDEF") for c in range(6)) # 6 random choices from possible chars for hex color

def turtlePattern(numIter, numSides, invert=False, fill=False, selColor=None, bgColor="#FFFFFF", func=lambda x: x, instant=True):
    invertMap = {True: -1, False: 1} # For reversing iterable
    hasColor = not not selColor # Covert selected color to boolean (if passed=true, v.v)

    # Set color to random if one not passed
    if hasColor:
        color = selColor
    else:
        color = generateHexColor() 

    # Setup turtle
    t = turtle.Turtle()
    t.speed('fastest')
    s = t.getscreen()
    s.bgcolor(bgColor)

    # Disable refresh if instant
    if instant:        
        s.tracer(0,0)

    for i in range(numIter)[::invertMap[invert]]: # Reverse iterable to start from highest value based on invert map

        if fill:
            t.begin_fill()
        for j in range(numSides):
            # Draw shape
            t.forward(func(i))
            t.left(360/numSides)
        
        if not hasColor:
            color = generateHexColor()
        if fill: 
            t.end_fill()

        t.color(color)
        t.fillcolor(color)
        t.left(360/numSides)

    # Refresh image
    s.update()