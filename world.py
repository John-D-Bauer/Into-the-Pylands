''' TODO:
    - Make different area instead of water
    - Add more colors instead of using termcolor
    - Make predetermined areas of the map
    - Combine both predetermined areas and random areas
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

        area_size = 29

        plain = self.buildRandArea("PLAIN", area_size, area_size)
        plain2 = self.buildRandArea("PLAIN", area_size, area_size)
        plain3 = self.buildRandArea("PLAIN", area_size, area_size)
        mount = self.buildRandArea("MOUNT", area_size, area_size)
        mount2 = self.buildRandArea("MOUNT", area_size, area_size)
        mount3 = self.buildRandArea("MOUNT", area_size, area_size)
        desert = self.buildRandArea("DSSRT", area_size, area_size)
        desert2 = self.buildRandArea("DSSRT", area_size, area_size)
        lake = self.buildRandArea("LAKES", area_size, area_size)

        biomes = [plain, plain2, plain3, mount, mount2, mount3, desert, desert2, lake]

        random.shuffle(biomes)

        biomeRowCnt = 0
        for biomeRowCnt in range(3):
            biomeRow = [biomes[biomeRowCnt*3], biomes[(biomeRowCnt*3) + 1], biomes[(biomeRowCnt*3) + 2]]
            for row, _ in enumerate(biomeRow[0]):
                for biome in biomeRow:
                    self.printRow(biome, row)
                print()
              

        #self._world = self.buildRandArea(81, 51)
            
    def printRow(self, area, row):
        cRow = []
        for t in area[row]:
            if t == "GRSS" or t == "SAND" or t == "GRVL":
                iter = random.choice(self.worldStrs[t])
                s = iter
            else:
                s = self.worldStrs[t]
            cRow.append(s)
                
        #os.system("cls")
        for s in cRow:
            print(s, end="")



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

    def buildRandArea(self, biome, width, height):
        randArea = self.createAltitude(biome, width, height)

        return randArea

    def createAltitude(self, biome, w, h):
        noise = PerlinNoise(octaves=15, seed=random.randint(0, 10000))

        randArea = []
        for y in range(h):
            altRow = []
            for x in range(w):
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

