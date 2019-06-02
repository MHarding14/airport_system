from passenger_class import Passenger
from plane_class import Plane


class Flight_Trip:

    def __init__(self, origin, destination, Plane,):
        self.origin = origin
        self.destination = destination
        self.plane = Plane
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f'{passenger} has been added to the flight')

