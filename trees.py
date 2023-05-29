import random
import turtle

class Tree():
    def __init__(self, burning=False, wetness=1.0, xpos=0, ypos=0):
        # Initialize Tree object with given parameters
        self.burning = burning
        self.wetness = wetness
        self.xpos = xpos
        self.ypos = ypos

    def changeBurning(self, burning):
        # Change the burning state of the tree
        self.burning = burning


class Oak(Tree):
    def __init__(self, burning=False, wetness=1.0, xpos=0, ypos=0):
        # Initialize Oak object with given parameters and additional properties
        super().__init__(burning, wetness, xpos, ypos)
        self.probCatch = 0.45 / wetness

    def draw(self):
        #Draw an Oak tree on the screen
        t = turtle
        t.hideturtle()
        t.penup()
        t.setpos(self.xpos, self.ypos)
        if not self.burning:
            t.color('green')
        else:
            t.color('red')
        t.shape('circle')
        t.shapesize(0.65)
        t.settiltangle(90)
        t.stamp()


class Fir(Tree):
    def __init__(self, burning=False, wetness=1.0, xpos=0, ypos=0):
        # Initialize Fir object with given parameters and additional properties
        super().__init__(burning, wetness, xpos, ypos)
        self.probCatch = 0.95 / wetness

    def draw(self):
        #Draw a Fir tree on the screen
        t = turtle
        t.hideturtle()
        t.penup()
        t.setpos(self.xpos, self.ypos)
        if not self.burning:
            t.color('green')
        else:
            t.color('red')
        t.shape('triangle')
        t.shapesize(0.65)
        t.settiltangle(90)
        t.stamp()