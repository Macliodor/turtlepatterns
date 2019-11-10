# TurtlePatterns

TurtlePatterns allows you to create geometric visualizations of mathematical functions using Python Turtle.


# Usage
Below is an example showing the usage of the tool:

    import turtlepatterns
    
    def square(x):
	    return x**2
	
	t = TurtlePatterns(numSides=4, color=None, bgColor="#ffffff")
	t.turtlePattern(numIter=20, invert=False, fill=True, func=square, instant=True)
	done()

 - By importing turtlepatterns, you are also importing the turtle module
   & random.choice.
   
 - Importing the file happens locally; make sure to reference the file correctly.
 - Lambda functions can also be used in replacement of defined functions, as seen below:
`turtlePattern(numIter=20, invert=False, fill=True, func=lambda x: x**2, instant=True)`
 - Adding the done() function will allow the graphics window to persist. This isn't neccesary unless you want to see the graphics created.

## Patterns

 - **shapePattern**: Generate shape pattern based on mathematical function. Coloring is either random or set to one color.
 - **modularPattern**: Same functionality as shapePattern, but colors based on divisibility by a passed integer.


## Demonstrations
This repository also contains a file called `demonstrations.py`. It contains numerous uses of the tool to create visualizations. You can use it as a starting ground to get familiar with the tool, or modify a use to create varying results.

The file is split up into sections based on the type of function being visualized (eg. linear, trigonometric, modular), & each use is labeled with its respective function.
