# do all imports
from aircraft_class import *
from plane_class import *
from passenger_class import *
from flight_trip_class import *

print('- create 3 planes')
concorde = Plane('Concorde', 500, 'Green')
print(concorde)
spitfire = Plane('Spitfire', 17, 'Blue')
print(spitfire)
tornado = Plane('Tornado', 150, 'Black')
print(tornado)
print('--------------------------------')

print('- create 3 passengers')
kirsty = Passenger('Kirsty Warner', 71563892, 'female', 24)
print(kirsty)
matt = Passenger('Matt Harding', 71598342, 'Male', 24)
print(matt)
scott = Passenger('Scott Williams', 63926178, 'Male', 45)
print(scott)
vanessa = Passenger('Vanessa Harding', 74652981, 'Female', 59)
print(vanessa)
print('--------------------------------')

print('- create flights then list available flights')
flight_1 = Flight_Trip('London', 'Madrid', concorde)
flight_2 = Flight_Trip('Paris', 'Lisbon', spitfire)
flight_3 = Flight_Trip('Rome', 'New York', tornado)
print('Flights created...')
flights_list = []
flights_list.append(flight_1)
flights_list.append(flight_2)
flights_list.append(flight_3)
print(flights_list)

