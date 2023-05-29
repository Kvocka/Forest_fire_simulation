import random
import turtle


# 0 = N, 1 = NE, 2 = E, 3 = SE, 4 = S, 5 = SW, 6 = W, 7 = NW

class Tree():
    def __init__(self, burning=False, wetness=1.0, windyness=0.0, xpos=0, ypos=0, probCatch=0):
        # Initialize Tree object with given parameters
        self.burning = burning
        self.wetness = wetness
        self.xpos = xpos
        self.ypos = ypos
        self.windyness = windyness
        self._probCatch = probCatch

    @property
    def probCatch(self):
        catchChange = self._probCatch / self.wetness
        return catchChange + self.windyness / 5

    def changeBurning(self, burning):
        # Change the burning state of the tree
        self.burning = burning


class Oak(Tree):
    def __init__(self, burning=False, wetness=1.0, windyness=0.0, xpos=0, ypos=0):
        # Initialize Oak object with given parameters and additional properties
        super().__init__(burning, wetness, windyness, xpos, ypos, 0.45)

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

    def __init__(self, burning=False, wetness=1.0, windyness=0.0, xpos=0, ypos=0):
        super().__init__(burning, wetness, windyness, xpos, ypos, 0.95)

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