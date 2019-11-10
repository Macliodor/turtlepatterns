import turtle
from random import choice


class TurtlePattern:

    def __init__(self, numSides, color=None, bgColor="#ffffff"):
        self.numSides = numSides
        self.color = color
        self.bgColor = bgColor
        self.invertMap = {True: -1, False: 1}

    def _generateHexColor(self):
        return "#" + "".join(choice("0123456789ABCDEF") for c in range(6)) # 6 random choices from possible chars for hex color


    def shapePattern(self, numIter, invert=False, fill=True, func=lambda x: x, instant=True):
         # For reversing iterable
        hasColor = not not self.color # Covert selected color to boolean (if passed=true, v.v)

        # Set color to random if one not passed
        if hasColor:
            color = self.color
        else:
            color = self._generateHexColor() 

        # Setup turtle
        t = turtle.Turtle()
        t.speed('fastest')
        s = t.getscreen()
        s.bgcolor(self.bgColor)

        # Disable refresh if instant
        if instant:        
            s.tracer(0,0)

        for i in range(numIter)[::self.invertMap[invert]]: # Reverse iterable to start from highest value based on invert map

            if fill:
                t.begin_fill()
            for j in range(self.numSides):
                # Draw shape
                t.forward(func(i))
                t.left(360/self.numSides)
            
            if not hasColor:
                color = self._generateHexColor()
            if fill: 
                t.end_fill()

            t.color(color)
            t.fillcolor(color)
            t.left(360/self.numSides)

        # Refresh image
        s.update()

