''' TODO:
    - Add preconfigured areas to whole map
    - Create biomes/altitudes to random map
    - 

'''

import random
import os
from termcolor import colored
from perlin_noise import PerlinNoise



class World:
    def __init__(self):
        self._worldW = 89
        self._worldH = 55
        self._world = self.buildWorld()

        self.worldStrs = {
            "GRSS" : [colored(", ", "green"), colored(" ,", "green"), colored(",,", "green")],
            "ROCK" : colored("88", "grey"),
            "WATR" : colored("≈≈", "blue"), 
            "LAVA" : colored("≈≈", "red"),
            "SAND" : [colored(", ", "yellow"), colored(" ,", "yellow"), colored(",,", "yellow")],
        }
        self._world = []

    def buildWorld(self):
        """
        Creates a world
        """

        #self._world = self.buildStartingArea()

        self._world = self.buildRandArea(self._worldW, self._worldH)

        #self._world = self.addTop(self._world, rTop)


    def buildStartingArea(self):
        start = [
            ["GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS"],
            ["ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "GRSS", "ROCK", "GRSS", "GRSS", "ROCK"],
            ["GRSS", "GRSS", "GRSS", "ROCK", "ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK"],
            ["ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "ROCK", "ROCK"],
            ["ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK"],
            ["ROCK", "GRSS", "ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "ROCK"],
            ["GRSS", "GRSS", "ROCK", "ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "ROCK", "GRSS"],
            ["GRSS", "GRSS", "ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "ROCK", "ROCK", "GRSS"],
            ["ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS"],
            ["ROCK", "ROCK", "GRSS", "GRSS", "ROCK", "GRSS", "GRSS", "GRSS", "ROCK", "GRSS", "ROCK"],
            ["GRSS", "GRSS", "ROCK", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "GRSS", "ROCK", "ROCK"],
            ["ROCK", "ROCK", "ROCK", "ROCK", "GRSS", "GRSS", "ROCK", "GRSS", "ROCK", "GRSS", "ROCK"],
        ]

        return start

    def buildRandArea(self, width, height):
        noise = PerlinNoise(octaves=15, seed=random.randint(0, 10000))

        randArea = []

        for y in range(height):
            row = []
            for x in range(width):
                noise_val = noise([x/width, y/height])
                if noise_val < 0.1:
                    row.append("GRSS")
                else:
                    row.append("ROCK")
            randArea.append(row)

        return randArea
        

    def printWorld(self):
        colorArea = []
        for row in self._world:
            newRow = []
            for t in row:
                if t == "GRSS" or t == "SAND":
                    iter = random.choice(self.worldStrs[t])
                    s = iter
                else:
                    s = self.worldStrs[t]
                newRow.append(s)
            colorArea.append(newRow)

        #os.system("cls")
        for row in colorArea:
            for s in row:
                print(s, end="")
            print()

