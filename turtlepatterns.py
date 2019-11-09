import turtle
from random import choice

def generateHexColor():
    return "#" + "".join(choice("0123456789ABCDEF") for c in range(6))
 
def turtlePattern(numIter, numSides, invert=False, fill=False, selColor=None, func=lambda x: x, instant=True):
    invertMap = {True: -1, False: 1}
    hasColor = not not selColor
    if hasColor:
        color = selColor
    else:
        color = generateHexColor()

    t = turtle.Turtle()
    t.speed('fastest')
    s = t.getscreen()
    if instant:        
        s.tracer(0,0)
    for i in range(numIter)[::invertMap[invert]]:
        if fill:
            t.begin_fill()
        for j in range(shapeSize):
            t.forward(func(i))
            t.left(360/shapeSize)
        
        if not hasColor:
            color = generateHexColor()
        if fill: 
            t.end_fill()
        t.color(color)
        t.fillcolor(color)
        t.left(360/numSides)
    s.update()