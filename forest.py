import random
import turtle
from trees import *

class Forest:
    def __init__(self):
        self.forestList = []

    def prompts(self):
        
        #Prompts for density, percentFir, and wetness, and returns values.
        
        density = float(input('What percentage of grid cells are occupied by trees? (0.10-1): '))
        percentFir = float(input('What percentage of trees are Fir? (0.00-1): '))
        wetness = float(input('How wet is the forest? (1-3), (1=dry, 3=wet): '))
        windyness = float(input('How windy is it? (0.00-1): '))
        return density, percentFir, wetness, windyness

    def initialize_forest_list(self, density, percentFir, wetness, windyness):
        
        #Adds trees to self.forestList based on density, percentFir, and wetness.
       
        for i in range(40):
            for j in range(40):
                random_density = random.uniform(0.1, 1)
                if random_density <= density:
                    random_fir = random.uniform(0.0, 1)
                    if random_fir <= percentFir:
                        obj = Fir(False, wetness, windyness, j, i)
                        self.addTree(obj)
                    else:
                        obj = Oak(False, wetness, windyness, j, i)
                        self.addTree(obj)
                else:
                    self.addTree(None)

    def initial_tree_on_fire(self):
        #Sets a random tree on fire.
        newList = [index for index, obj in enumerate(self.forestList) if obj is not None]
        number = random.randint(0, len(newList) - 1)
        fire_index = newList[number]
        self.forestList[fire_index].changeBurning(True)

    def addTree(self, obj):
        
        #Adds a tree to the forest.
        
        self.forestList.append(obj)

    def removeTree(self, index):
        
        #Removes a tree from the forest.
        
        self.forestList[index] = None

    def update(self):
        
        #Updates the burning status of trees in the forest.
        
        oldBurningTrees = []
        newBurningTrees = []
        forestlist = self.getForestList()
        for i, obj in enumerate(forestlist):
            if obj is not None:
                if obj.burning:
                    oldBurningTrees.append(i)
                else:
                    random_num = random.random()
                    if random_num < obj.probCatch and self.hasBurningNeighbor(obj):
                        newBurningTrees.append(i)
        for i in oldBurningTrees:
            forestlist[i] = None
        for i in newBurningTrees:
            obj = forestlist[i]
            obj.burning = True
        self.forestList = forestlist

    def getForestList(self):
        
        #Returns the forest list.
        return self.forestList

    #Returns True if a tree is burning in the forest, False otherwise.
    def isBurning(self):
        for obj in self.forestList:
            if obj is not None and obj.burning:
                return True
        return False

    #Checks if any neighbors are burning.
    def hasBurningNeighbor(self, obj):
        for tree in self.forestList:
            if tree is not None and obj is not None:
                if tree is obj:
                    continue
                elif (tree.xpos - obj.xpos) in range(-1, 2) and (tree.ypos - obj.ypos) in range(-1, 2):
                    if tree.burning:
                        return True

    #Redraws the graphic display.
    def redraw(self):
        turtle.clearstamps()
        turtle.tracer(0, 0)
        for obj in self.forestList:
            if obj is not None:
                obj.draw()
        turtle.update()