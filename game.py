from world import World
from player import Player
import os


world = World()
#player = Player(input("Please enter two characters to represent your character: "))

def main():
    start()

    update()

    

def start():
    with open(r"C:\Users\John\Documents\Coding Projects\Into the Pylands\.vscode\settings.json", "w") as json_file:
        json_file.write('{"terminal.integrated.fontSize": 14}')
        

    world.buildWorld()
    

def update():
    #world.printWorld(world._world)

    if True: #This determines when the game ends
        with open(r"C:\Users\John\Documents\Coding Projects\Into the Pylands\.vscode\settings.json", "w") as json_file:
            json_file.write('{"terminal.integrated.fontSize": 14}')

    


if __name__ == "__main__":
    main()
