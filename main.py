from forest import *
from trees import *
from time import sleep
import turtle

def main():
    t = turtle
    f = Forest()
    density, percentFir, wetness, windyness = f.prompts()
    f.initialize_forest_list(density, percentFir, wetness, windyness)
    f.initial_tree_on_fire()
    t.setworldcoordinates(0, 0, 40, 40)
    f.redraw()
    done = False
    while not done:
        f.update()
        sleep(0.1)
        f.redraw()
        if not f.isBurning():
            done = True
    sleep(5)

if __name__=="__main__":
    main()
