# TurtlePatterns

TurtlePatterns allows you to create geometric visualizations of mathematical functions using Python Turtle.


# Usage
Below is an example showing the usage of the tool:

    import turtlepatterns
    
    def square(x):
	    return x**2
	
	turtlePattern(numIter=20, numSides=4, invert=False, fill=True, selColor="#000000",func=square,instant=True)
	done()

 - By importing turtlepatterns, you are also importing the turtle module
   & random.choice.
   
 - Importing the file happens locally; make sure to reference the file correctly.
 - Lambda functions can also be used in replacement of defined functions, as seen below:
`turtlePattern(numIter=20, numSides=4, invert=False, fill=True, selColor="#000000",func=lambda x: x**2,instant=True)`
 - Adding the done() function will allow the graphics window to persist. This isn't neccesary unless you want to see the graphics created.

## Arguments
Below are the arguments you can specify for the function:

 - **numIter (int)**: The number of shapes to create. This will also define the maximum shape size as given by the function passed to the tool.
 - **numSides (int)**: The shape to use based on the number of sides. (eg. Square=4, Octagon=8)
 - **invert (boolean)**: Whether to draw the shapes in descending or ascending size. 
 - **fill (boolean)**: Whether to add a fill color to the shape. Setting this value to *True* will fill the shapes based on the color being used to draw them.
 - **selColor (Hex color in string, None)**: Whether to use a given color to draw the shapes. Setting this value to *None* will allow random color generation.
 - **func (Function, lambda function)**: The function to be used in drawing. Can be a defined function or lambda function (As seen in [Usage](#usage) section).
 - **instant (boolean)**: Whether to draw the shape instantly


## Demonstrations
This repository also contains a file called `demonstrations.py`. It contains numerous uses of the tool to create visualizations. You can use it as a starting ground to get familiar with the tool, or modify a use to create varying results.

The file is split up into sections based on the type of function being visualized (eg. linear, trigonometric, modular), & each use is labeled with its respective function.
