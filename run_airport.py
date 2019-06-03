# do all imports
from aircraft_class import *
from plane_class import *
from helicopter_class import *
from passenger_class import *
from flight_trip_class import *

print('-- create 3 planes --')
print('Planes:')
concorde = Plane('Concorde', 500, 'Green')
print(concorde.name)
spitfire = Plane('Spitfire', 17, 'Blue')
print(spitfire.name)
tornado = Plane('Tornado', 150, 'Black')
print(tornado.name)
print('--------------------------------')

print('- create 3 passengers -')
print('Passengers:')
kirsty = Passenger('Kirsty Warner', 71563892, 'female', 24)
print(kirsty.name)
matt = Passenger('Matt Harding', 71598342, 'Male', 24)
print(matt.name)
scott = Passenger('Scott Williams', 63926178, 'Male', 45)
print(scott.name)
vanessa = Passenger('Vanessa Harding', 74652981, 'Female', 59)
print(vanessa.name)
joanna = Passenger('Joanna Thompson', 87235731, 'Female', 83)
burt = Passenger('Burt Kuman', 78925146, 'Male', 43)
print(burt)
print('--------------------------------')


print('- create flights then list available flights')
flight_1 = Flight_Trip('BA2703', 'London', 'Madrid', concorde)
flight_2 = Flight_Trip('RY9876', 'Paris', 'Lisbon', spitfire)
flight_3 = Flight_Trip('DE1408', 'Rome', 'New York', tornado)
print('Available flights:')
flights_list = []
flights_list.append(flight_1)
flights_list.append(flight_2)
flights_list.append(flight_3)
for flight in flights_list:
    print(flight.flight_num)
print('--------------------------------')

helicopter_1 = Helicopter('Hell', 7, 'Black')
print(helicopter_1.hover())
print('--------------------------------')

print('-- add passenger to flight --')
flight_1.add_passenger(kirsty)
print(flight_1.passengers[0].name)

print('--------------------------------')

