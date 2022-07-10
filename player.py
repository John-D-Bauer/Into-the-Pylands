from world import World

class Player:
    def __init__(self, image):
        world = World()
        self._image = image
        self._x = int(world._worldW/2)
        self._y = int(world._worldH/2)
        self._hp = 100 
