import numpy as np
from PIL import Image


class Canvas:
    """
    Creates canvas where all shapes wil be drawn.
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Creates a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Converts the current array into an image file.
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:
    """
    A rectangle shape that can be drawn on a canvas object
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """ Draws itself onto the canvas """
        # Changes a slice of array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """ Draws itself onto the canvas """
        # Changes a slice of array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


# Get canvas width and height from user
canvas_width = int(input("Enter a canvas width: "))
canvas_height = int(input("Enter a canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw (square or rectangle)? Enter quit to exit. ")

    # Ask for rectangle data and create rectangle if user entered "rectangle"
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter a X of Rectangle: "))
        rec_y = int(input("Enter a Y of Rectangle: "))
        rec_width = int(input("Enter a width of Rectangle: "))
        rec_height = int(input("Enter a height of Rectangle: "))
        red = int(input("How dark red color should be on the scale between 0 to 255? "))
        blue = int(input("How dark blue color should be on the scale between 0 to 255? "))
        green = int(input("How dark green color should be on the scale between 0 to 255? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered "square"
    if shape_type.lower() == 'square':
        squ_x = int(input("Enter a X of Square: "))
        squ_y = int(input("Enter a Y of Square: "))
        squ_side = int(input("Enter a side of Square: "))
        red = int(input("How dark red color should be on the scale between 0 to 255? "))
        blue = int(input("How dark blue color should be on the scale between 0 to 255? "))
        green = int(input("How dark green color should be on the scale between 0 to 255? "))

        # Create the rectangle
        s1 = Square(x=squ_x, y=squ_y, side=squ_side, color=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shape_type.lower() == 'quit':
        break

canvas.make("canvas.png")
