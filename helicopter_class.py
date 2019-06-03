from aircraft_class import Aircraft

class Helicopter(Aircraft):

    def __init__(self, name, capacity, colour = ''):
        self.colour = colour
        self.name = name
        self.blades = 4
        self.capacity = capacity

    def hover(self):
        return("Look, I'm going nowhere...")

