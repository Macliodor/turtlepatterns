# === DEMONSTRATIONS ===
# All functions in this file are inverted, use squares, use fill, use random colors, are instantly drawn, & have 20 iterations.
# Modular patterns use a divider of 3.

from turtlepatterns import *
import math
import random


t = TurtlePatterns(numSides=4, color=None, bgColor="#ffffff")

# === LINEAR ===
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: x, instant=True) # Linear w/ slope of 1
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 2*x, instant=True) # Linear w/ slope of 2
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 0.5*x, instant=True) # Linear w/ slope of 1/2

# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: x, instant=True, divider=3) # Linear w/ slope of 1
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 2*x, instant=True, divider=3) # Linear w/ slope of 2
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 0.5*x, instant=True, divider=3) # Linear w/ slope of 1/2

# === POLYNOMIAL ===
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: x**2, instant=True) # Squared
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: x**3, instant=True) # Cubed
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: x**4, instant=True) # Fourth Power

# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: x**2, instant=True, divider=3) # Squared
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: x**3, instant=True, divider=3) # Cubed
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: x**4, instant=True, divider=3) # Fourth Power

# === EXPONENTIAL ===
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 2**x, instant=True) # 2^x
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 3**x, instant=True) # 3^x
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: math.exp(x), instant=True) # e^x

# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 2**x, instant=True, divider=3) # 2^x
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 3**x, instant=True, divider=3) # 3^x
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: math.exp(x), instant=True, divider=3) # e^x

# === TRIGONOMETRIC ===
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 50*math.sin(x), instant=True) # Sine
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: 50*math.cos(x), instant=True) # Cosine

# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 50*math.sin(x), instant=True, divider=3) # Sine
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: 50*math.cos(x), instant=True, divider=3) # Cosine

# === MODULAR ===
# t.shapePattern(numIter=200, invert=True, fill=True, func=lambda x: x*(x%2), instant=True) # x mod 2 (divisible by 2)
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: x*(x%6), instant=True) # x mod 6 (divisibile by 6)

# t.modularPattern(numIter=200, invert=True, fill=True, func=lambda x: x*(x%2), instant=True, divider=3) # x mod 2 (divisible by 2)
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: x*(x%6), instant=True, divider=3) # x mod 6 (divisibile by 6)

# === RANDOM ===
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: random.randint(1,100), instant=True) # Random size from 1 to 100
# t.shapePattern(numIter=20, invert=True, fill=True, func=lambda x: random.randint(1,500), instant=True) # Random size from 1 to 500

# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: random.randint(1,100), instant=True, divider=3) # Random size from 1 to 100
# t.modularPattern(numIter=20, invert=True, fill=True, func=lambda x: random.randint(1,500), instant=True, divider=3) # Random size from 1 to 500
turtle.done()