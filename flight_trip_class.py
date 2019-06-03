from passenger_class import Passenger
from plane_class import Plane


class Flight_Trip:

    def __init__(self, flight_num = '', origin = '', destination = '', plane = ''):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f'{passenger} has been added to the flight')

    def add_plane(self, plane):
        self.plane = plane

    def add_origin(self, origin):
        self.origin = origin

    def add_destination(self, destination):
        self.destination = destination

    def add_flight_num(self, flight_num):
        self.flight_num = flight_num
