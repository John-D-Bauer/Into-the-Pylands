''' TODO:
    - Determine how big the world should actually be
    - Make predetermined areas of the map
    - Combine both predetermined areas and random areas
'''

import random
import os
from perlin_noise import PerlinNoise

class World:
    def __init__(self):
        self._world = []
        self._worldH = 19*3
        self._worldW = 19*3

        self.worldStrs = {
            "GRSS" : ["\033[38;5;2m, ", "\033[38;5;2m ,", "\033[38;5;2m,,"],
            "ROCK" : "\033[38;5;243m88",
            "LAVA" : "\033[38;5;1m≈≈",
            "WATR" : "\033[38;5;4m≈≈",
            "GRVL" : ["\033[38;5;232m, ", "\033[38;5;232m ,", "\033[38;5;232m,,"],
            "SAND" : ["\033[38;5;3m, ", "\033[38;5;3m ,", "\033[38;5;3m,,"],
            "SNOW" : ["\033[38;5;231m, ", "\033[38;5;231m ,", "\033[38;5;231m,,"],
            "ICEY" : "\033[38;5;32m88",
        }

    def buildWorld(self):
        """
        Creates a world
        """

        #self._world = self.buildStartingArea()

        area_size = 19

        plain = self.buildRandArea("PLAIN", area_size, area_size)
        plain2 = self.buildRandArea("PLAIN", area_size, area_size)
        plain3 = self.buildRandArea("PLAIN", area_size, area_size)
        mount = self.buildRandArea("MOUNT", area_size, area_size)
        mount2 = self.buildRandArea("MOUNT", area_size, area_size)
        desert = self.buildRandArea("DSSRT", area_size, area_size)
        desert2 = self.buildRandArea("DSSRT", area_size, area_size)
        snow = self.buildRandArea("SNOWY", area_size, area_size)
        snow2 = self.buildRandArea("SNOWY", area_size, area_size)

        biomes = [plain, plain2, plain3, mount, mount2, desert, desert2, snow, snow2]

        random.shuffle(biomes)

        self._world = self.addBiomes(biomes)

        self._worldW = len(self._world[0])
        self._worldH = len(self._world)

            
    def addRow(self, area, row):
        cRow = []
        for t in area[row]:
            if t == "GRSS" or t == "SAND" or t == "GRVL" or t == "SNOW":
                iter = random.choice(self.worldStrs[t])
                s = iter
            else:
                s = self.worldStrs[t]
            cRow.append(s)
        return cRow

    def addBiomes(self, biomes):
        biomeRowCnt = 0
        newWorld = []
        for biomeRowCnt in range(3):
            biomeRow = [biomes[biomeRowCnt*3], biomes[(biomeRowCnt*3) + 1], biomes[(biomeRowCnt*3) + 2]]
            for row, _ in enumerate(biomeRow[0]):
                newRow = []
                for biome in biomeRow:
                    newRow += self.addRow(biome, row)
                newWorld.append(newRow)
        return newWorld



    def buildStartingArea(self):
        return [
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
                elif biome == "SNOWY":
                    if noise_val < 0.2:
                        altRow.append("SNOW")
                    else:
                        altRow.append("ICEY")
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
        #os.system("cls")
        for row in area:
            for s in row:
                print(s, end="")
            print("\033[38;5;7m")

