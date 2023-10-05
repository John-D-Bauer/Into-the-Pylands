from world import World
from player import Player



world = World()
player = Player(input("Please enter two characters to represent your character: "))

def main():
    start()

    update()

    

def start():
    with open(r"C:\Users\John\Documents\Coding Projects\Into the Pylands\.vscode\settings.json", "w") as json_file:
        json_file.write('{"terminal.integrated.fontSize": 14}')
    
    world.buildWorld()
    player.pworld.printWorld(player.pworld._world)
    

def update():
    print("\033[38;5;7m")
    player.printPlayerView()
    print("\033[38;5;7m")
    player.updatePlayerPos()


    print("\033[38;5;7m")

    if True: #This determines when the game ends
        with open(r"C:\Users\John\Documents\Coding Projects\Into the Pylands\.vscode\settings.json", "w") as json_file:
            json_file.write('{"terminal.integrated.fontSize": 14}')

    


if __name__ == "__main__":
    main()
