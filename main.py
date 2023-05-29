from forest import *
from trees import *
import turtle

def main():
    t = turtle
    f = Forest()
    density, percentFir, wetness = f.prompts()
    f.initialize_forest_list(density, percentFir, wetness)
    f.initial_tree_on_fire()
    t.setworldcoordinates(0, 0, 40, 40)
    f.redraw()
    done = False
    while not done:
        f.update()
        f.redraw()
        if not f.isBurning():
            done = True

if __name__=="__main__":
    while True:
        main()
