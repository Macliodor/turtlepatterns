# === DEMONSTRATIONS ===
# All functions in this file are inverted, use squares, use fill, use random colors, are instantly drawn, & have 20 iterations.

from turtlepatterns import *
import math
import random

# === LINEAR ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: x, instant=True) # Linear w/ slope of 1
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 2*x, instant=True) # Linear w/ slope of 2
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 0.5*x, instant=True) # Linear w/ slope of 1/2

# === POLYNOMIAL ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: x**2, instant=True) # Squared
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: x**3, instant=True) # Cubed
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: x**4, instant=True) # Fourth Power

# === EXPONENTIAL ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 2**x, instant=True) # 2^x
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 3**x, instant=True) # 3^x
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: math.exp(x), instant=True) # e^x

# === TRIGONOMETRIC ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 50*math.sin(x), instant=True) # Sine
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 50*math.cos(x), instant=True) # Cosine

# === MODULAR ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 50*(x%2), instant=True) # x mod 2 (divisible by 2)
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: 50*(x%6), instant=True) # x mod 6 (divisibile by 6)

# === RANDOM ===
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: random.randint(1,100), instant=True) # Random size from 1 to 100
# turtlePattern(numIter=20, numSides=4, invert=True, fill=True, selColor=None, func=lambda x: random.randint(1,500), instant=True) # Random size from 1 to 500

turtle.done()