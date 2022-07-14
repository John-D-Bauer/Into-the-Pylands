''' TODO:
    - Add preconfigured areas to whole map
    - Create blocks of designed or random areas
    - Randomly assign those blocks
'''

import random
import os
from termcolor import colored
from perlin_noise import PerlinNoise



class World:
    def __init__(self):
        self._worldW = 89
        self._worldH = 55
        self._world = []

        self.worldStrs = {
            "GRSS" : [colored(", ", "green"), colored(" ,", "green"), colored(",,", "green")],
            "ROCK" : colored("88", "grey"),
            "WATR" : colored("≈≈", "blue"), 
            "LAVA" : colored("≈≈", "red"),
            "GRVL" : [colored(", ", "grey"), colored(" ,", "grey"), colored(",,", "grey")],
            "SAND" : [colored(", ", "yellow"), colored(" ,", "yellow"), colored(",,", "yellow")],
        }

    def buildWorld(self):
        """
        Creates a world
        """

        #self._world = self.buildStartingArea()

        # plain = self.buildRandArea("PLAIN", 11, 11)
        # plain2 = self.buildRandArea("PLAIN", 11, 11)
        # plain3 = self.buildRandArea("PLAIN", 11, 11)
        # mount = self.buildRandArea("MOUNT", 11, 11)
        # mount2 = self.buildRandArea("MOUNT", 11, 11)
        # mount3 = self.buildRandArea("MOUNT", 11, 11)
        # desert = self.buildRandArea("DSSRT", 11, 11)
        # desert2 = self.buildRandArea("DSSRT", 11, 11)
        # lake = self.buildRandArea("LAKES", 11, 11)

        #biomes = [plain, plain2, plain3, mount, mount2, mount3, desert, desert2, lake]

        #random.shuffle(biomes)

        # for biome in biomes:
        #     self.printWorld(biome)

        self._world = self.buildRandArea(81, 51)
            
        


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
        bWorld = self.createBiomes(width, height)
        randArea = self.createAltitude(bWorld, width, height)

        return randArea

    def createBiomes(self, w, h):
        biomes = PerlinNoise(octaves=4, seed=random.randint(0, 10000))
        bWorld = []
        for y in range(h):
            row = []
            for x in range(w):
                noise_val = biomes([x/w, y/h])
                if noise_val < 0.1:
                    row.append("PLAIN")
                elif noise_val < 0.15:
                    row.append("LAKES")
                elif noise_val < 0.35:
                    row.append("MOUNT")
                else:
                    row.append("DSSRT")
            bWorld.append(row)
        return bWorld

    def createAltitude(self, world, w, h):
        noise = PerlinNoise(octaves=15, seed=random.randint(0, 10000))

        randArea = []
        for y, row in enumerate(world):
            altRow = []
            for x, biome in enumerate(row):
                noise_val = noise([x/w, y/h])

                if biome == "PLAIN":
                    if noise_val < 0.1:
                        altRow.append("GRSS")
                    else:
                        altRow.append("ROCK")
                elif biome == "LAKES":
                    altRow.append("WATR")
                elif biome == "MOUNT":
                    if noise_val < 0.15:
                        altRow.append("GRVL")
                    else:
                        altRow.append("LAVA")
                else:
                    if noise_val < 0.3:
                        altRow.append("SAND")
                    else:
                        altRow.append("ROCK")

            randArea.append(altRow)

        return randArea

        

    def printWorld(self, area):
        colorArea = []
        for row in area:
            newRow = []
            for t in row:
                if t == "GRSS" or t == "SAND" or t == "GRVL":
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

