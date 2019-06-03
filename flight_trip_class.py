from passenger_class import Passenger
from plane_class import Plane


class Flight_Trip:

    def __init__(self, num, origin, destination, plane):
        self.flight_num = ''
        self.origin = ''
        self.destination = ''
        self.plane = ''
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f'{passenger} has been added to the flight')

