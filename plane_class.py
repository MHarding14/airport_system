from aircraft_class import Aircraft

class Plane(Aircraft):

    def __init__(self, name, capacity, colour = ''):
        self.colour = colour
        self.name = name
        self.wings = 2
        self.capacity = capacity

