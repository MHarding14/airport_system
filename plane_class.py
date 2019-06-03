from aircraft_class import Aircraft

class Plane(Aircraft):

    plane_instances = []

    def __init__(self, name, capacity = 0, colour = ''):
        super().__init__()
        Plane.plane_instances.append(self)
        self.colour = colour
        self.name = name
        self.wings = 2
        self.capacity = capacity

