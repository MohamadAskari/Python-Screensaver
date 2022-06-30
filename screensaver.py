from tkinter import *
from random import *

# Base class
class Shape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.screenWidth = canvas.winfo_screenwidth()
        self.screenHeight = canvas.winfo_screenheight()
        self.randValues()
        self.randColor()
        self.createShape()

    # Randomize values for the shape coordinates
    def randValues(self):
        pass

    # Create the shape
    def createShape(self):
        pass

    # Move the shape in the screen
    def moveShape(self):
        pass

    # Check if the shape is goint out of the screen
    def findBoundry(self):
        pass

    # Randomize the color of the shape
    def randColor(self):
        self.color = choice(["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white", "aqua", "brown", "grey", "indigo", "lime", "magenta", "navy", "olive", "orange", "orchid", "salmon", "silver", "teal"])



# Below is the implentation of the 3 different shapes inherited from the Shape, each with their own random values. The constructors are implemented using inheritance.
# ----------------------------------------------------------------------------------------------------------------------------------------------

class Triangles(Shape):
    def __init__(self, canvas):
        Shape.__init__(self, canvas)

    def randValues(self):
        self.r = randint(100, 120)
        self.x1 = randint(100, 400)
        self.y1 = randint(200, 500)
        self.x2 = randint(100, 400)
        self.y2 = randint(200, 500)
        self.x3 = randint(100, 400)
        self.y3 = randint(200, 500)
        self.x_speed = randint(1, 10)
        self.y_speed = randint(1, 10)

    def createShape(self):
        self.triangle = self.canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill=self.color, outline=self.color)
        self.moveShape()

    def moveShape(self):
        self.findBoundry()
        self.x1 += self.x_speed
        self.x2 += self.x_speed
        self.x3 += self.x_speed
        self.y1 += self.y_speed
        self.y2 += self.y_speed
        self.y3 += self.y_speed
        self.canvas.move(self.triangle, self.x_speed, self.y_speed)

    def findBoundry(self):
        pass
        if self.x1 > self.screenWidth:
            self.x_speed = -self.x_speed
        elif self.x1 < 0:
            self.x_speed = -self.x_speed
        if self.y1 > self.screenHeight:
            self.y_speed = -self.y_speed
        elif self.y1 < 0:
            self.y_speed = -self.y_speed
        if self.x2 > self.screenWidth:
            self.x_speed = -self.x_speed
        elif self.x2 < 0:
            self.x_speed = -self.x_speed
        if self.y2 > self.screenHeight:
            self.y_speed = -self.y_speed
        elif self.y2 < 0:
            self.y_speed = -self.y_speed
        if self.x3 > self.screenWidth:
            self.x_speed = -self.x_speed
        elif self.x3 < 0:
            self.x_speed = -self.x_speed
        if self.y3 > self.screenHeight:
            self.y_speed = -self.y_speed
        elif self.y3 < 0:
            self.y_speed = -self.y_speed


class Sqaures(Shape):
    def __init__(self, canvas):
        Shape.__init__(self, canvas)

    def randValues(self):
        self.length = randint(100, 250)
        self.x1 = randint(100, 400)
        self.y1 = randint(200, 500)
        self.x2 = self.x1 + self.length
        self.y2 = self.y1 + self.length
        self.x_speed = randint(1, 10)
        self.y_speed = randint(1, 10)

    def createShape(self):
        self.rectangle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.color)
        self.moveShape()

    def moveShape(self):
        self.findBoundry()
        self.x1 += self.x_speed
        self.x2 += self.x_speed
        self.y1 += self.y_speed
        self.y2 += self.y_speed
        self.canvas.move(self.rectangle, self.x_speed, self.y_speed)

    def findBoundry(self):
        if self.x1 > self.screenWidth:
            self.x_speed = -self.x_speed
        elif self.x1 < 0:
            self.x_speed = -self.x_speed
        if self.y1 > self.screenHeight:
            self.y_speed = -self.y_speed
        elif self.y1 < 0:
            self.y_speed = -self.y_speed
        if self.x2 > self.screenWidth:
            self.x_speed = -self.x_speed
        elif self.x2 < 0:
            self.x_speed = -self.x_speed
        if self.y2 > self.screenHeight:
            self.y_speed = -self.y_speed
        elif self.y2 < 0:
            self.y_speed = -self.y_speed


class Balls(Shape):
    def __init__(self, canvas):
        Shape.__init__(self, canvas)
    
    def randValues(self):
        self.radius = randint(50, 100)
        self.x_coord = randint(self.radius, self.screenWidth - self.radius)
        self.y_coord = randint(self.radius, self.screenHeight - self.radius)
        self.x_speed = randint(1, 10)
        self.y_speed = randint(1, 10)
        self.color = choice(["red", "green", "blue", "yellow", "orange", "purple", "pink", "black",  "white"])

    def createShape(self):
        x1 = self.x_coord - self.radius
        y1 = self.y_coord - self.radius 
        x2 = self.x_coord + self.radius
        y2 = self.y_coord + self.radius
        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
    
    def moveShape(self):
        self.findBoundry()
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed
        self.canvas.move(self.ball, self.x_speed, self.y_speed)

    def findBoundry(self):
        if not self.radius < self.x_coord < self.screenWidth - self.radius:
            self.x_speed = -self.x_speed

        if not self.radius < self.y_coord < self.screenHeight - self.radius:
            self.y_speed = -self.y_speed


# End of implementation of shapes
# ----------------------------------------------------------------------------------------------------------------------------------------------


# Screen class
class Screen:  
    shapes = []

    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.8)
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=1, fill="both")

        Balls(self.canvas)
        Sqaures(self.canvas)
        Triangles(self.canvas)

        self.ball = Balls(self.canvas) 
        self.rectangle = Sqaures(self.canvas)
        self.triangle = Triangles(self.canvas)

        for i in range(6):
            self.shapes.append(Balls(self.canvas))
            self.shapes.append(Sqaures(self.canvas))
            self.shapes.append(Triangles(self.canvas)) 

        self.moveShapes()
        self.root.mainloop()

    # Move the shapes(Due to polymorphism, the "moveShape" method works for all kind of shapes)
    def moveShapes(self):
        for shape in self.shapes:
            shape.moveShape()
        self.root.after(30, self.moveShapes)


# Create a window
Screen()

