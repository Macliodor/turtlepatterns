from turtlepatterns import *
import math
import random
import time


t = TurtlePatterns(numSides=3, color=None, bgColor="#000000")


def modTesting(numDividerMax, sides):
	for i in range(0, numDividerMax+1):
		t.numSides = sides
		t.modularPattern(numIter=200, invert=True, fill=True, func=lambda x: x, instant=True, divider=sides+i)
		time.sleep(5)
		t.turtle.reset()

modTesting(5, 5)
turtle.done()