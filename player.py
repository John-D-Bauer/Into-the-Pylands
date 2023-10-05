''' TODO:
    - Determine collisions when player contacts obstacle
'''
import os
from world import World

class Player:

    def __init__(self, image):
        self.pworld = World()
        self.pworld.buildWorld()

        self._image = image
        self._x = 28
        self._y = 28
        self._hp = 100
        self._viewSize = 5

    

    def printPlayerView(self):
        tileCnt = 0

        for y in range(self._viewSize):
            for x in range(self._viewSize):
                print("\033[38;5;7m", end="")
                if (x == 2) and (y == 2):
                    print(self._image, end="")
                else:
                    print(self.pworld._world[self._y+y][self._x+x], end="")
                tileCnt += 1
                if tileCnt == 5:
                    print()
                    tileCnt = 0
        
    def updatePlayerPos(self):
        command =  input("What should you do? ").strip().capitalize()

        while command != "Q":

            if(command == "L"):
                self._x -= 1
            elif(command == "R"):
                self._x += 1
            elif(command == "U"):
                self._y -= 1
            elif(command == "D"):
                self._y += 1

            os.system("cls")
            self.printPlayerView()
            print("\033[38;5;7m")
            command =  input("What should you do? ").strip().capitalize()



