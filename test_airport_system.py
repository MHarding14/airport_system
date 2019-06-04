from run_airport import *
from passenger_class import *
from flight_trip_class import *
import pytest

# -----------Tests-----
#----------Passengers-----------
# I can create a passenger
# Create with a name and Passport number
# I can create 'Joanna Thompson' with passport no. 87235731
# I can create 'Burt Kuman' with passport no. 78925146
test_passenger = Passenger('Tester', 92847365, 'Male', 26)
test_passenger1 = Passenger('Tester1', 92847366, 'Male', 27)
test_passenger2 = Passenger('Tester2', 92847367, 'Male', 28)

def test_passenger_create():
    assert isinstance (test_passenger1, Passenger)

def test_passengers1():

    assert [test_passenger1.name, test_passenger1.passport_no] == ['Tester1', 92847366]

def test_passengers2():
    joanna = Passenger('Joanna Thompson', 87235731, 'Female', 83)

    assert [joanna.name, joanna.passport_no] == ['Joanna Thompson', 87235731]

def test_passengers3():
    burt = Passenger('Burt Kuman', 78925146, 'Male', 43)

    assert [burt.name, burt.passport_no] == ['Burt Kuman', 78925146]

# I get an error if passenger is created without name or passport number
        # Test for it breaking!
def test_passenger_break():
    with pytest.raises(TypeError):
        joe = Passenger()


#-----------Planes--------------
# I can create a plane with a plane number
def test_create_plane():

    jumbo_jet = Plane('Jumbo Jet', 900, 'multi-colour')

    assert [jumbo_jet.name, jumbo_jet.capacity, jumbo_jet.colour] == ['Jumbo Jet', 900, 'multi-colour']



#-----------Flight_trips--------
# I can create a flight with no specific information
def test_create_flight():
    test_flight = Flight_Trip()

    assert isinstance (test_flight, Flight_Trip)

# I can add a plane to the flight
def test_add_plane():
    test_flight = Flight_Trip()
    test_plane = Plane('Test Plane')
    test_flight.add_plane(test_plane)

    assert test_flight.plane == test_plane
# I can add a destination
def test_add_destination():
    test_flight = Flight_Trip()
    test_flight.add_destination('Madrid')

    assert test_flight.destination == 'Madrid'
# I can add an origin
def test_add_origin():
    test_flight = Flight_Trip()
    test_flight.add_origin('Heathrow')

    assert test_flight.origin == 'Heathrow'

# I can add a passenger to the passengers list
def test_add_passenger():
    test_flight = Flight_Trip()
    test_flight.add_passenger(test_passenger)

    assert test_flight.passengers[-1].name == test_passenger.name

# Passenger list is a list of objects that are passengers
def test_passengers_list():
    test_flight = Flight_Trip()
    test_flight.add_passenger(test_passenger1)
    test_flight.add_passenger(test_passenger2)

    assert type(test_flight.passengers) == list