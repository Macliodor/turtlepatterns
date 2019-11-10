import turtle
from random import choice


class TurtlePatterns:

    def __init__(self, numSides, color=None, bgColor="#ffffff"):
        self.numSides = numSides
        self.color = color
        self.bgColor = bgColor
        self.invertMap = {True: -1, False: 1}
        self.turtle = turtle.Turtle()

    def _generateHexColor(self):
        return "#" + "".join(choice("0123456789ABCDEF") for c in range(6)) # 6 random choices from possible chars for hex color

    def _generateModularColorMap(self, n):
        colormap = {}
        for i in range(n+1):
            colormap[i] = self._generateHexColor()
        return colormap


    def shapePattern(self, numIter, invert=False, fill=False, func=lambda x: x, instant=True):
         # For reversing iterable
        hasColor = not not self.color # Covert selected color to boolean (if passed=true, v.v)

        # Set color to random if one not passed
        if hasColor:
            color = self.color
        else:
            color = self._generateHexColor() 

        # Setup turtle
        self.turtle.speed('fastest')
        s = self.turtle.getscreen()
        s.bgcolor(self.bgColor)

        # Disable refresh if instant
        if instant:        
            s.tracer(0,0)

        for i in range(numIter)[::self.invertMap[invert]]: # Reverse iterable to start from highest value based on invert map

            if fill:
                self.turtle.begin_fill()
            for j in range(self.numSides):
                # Draw shape
                self.turtle.forward(func(i))
                self.turtle.left(360/self.numSides)
            if not hasColor:
                color = self._generateHexColor()
            if fill: 
                self.turtle.end_fill()

            self.turtle.color(color)
            self.turtle.fillcolor(color)
            self.turtle.left(360/self.numSides)

        # Refresh image
        s.update()
        self.turtle = turtle.Turtle() # Reset turtle

    def modularPattern(self, numIter, invert=False, fill=False, func=lambda x: x, instant=True, divider=2):

        colormap = self._generateModularColorMap(divider) # Generates colors based on num mod divider

        self.turtle = turtle.Turtle()
        self.turtle.speed(100)
        s = self.turtle.getscreen()
        s.bgcolor(self.bgColor)

        if instant:        
            s.tracer(0,0)

        for i in range(numIter)[::self.invertMap[invert]]:

            color = colormap[i%divider] # Get color for line based on divisibility from color map
            self.turtle.color(color)

            if fill:
                self.turtle.fillcolor(color)
                self.turtle.begin_fill()

            for j in range(self.numSides):
                self.turtle.forward(func(i))
                self.turtle.left(360/self.numSides)

            if fill: 
                self.turtle.end_fill()

            self.turtle.left(360/self.numSides)
        s.update()
        self.turtle = turtle.Turtle() 