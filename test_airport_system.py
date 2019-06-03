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

def test_passenger_create():
    assert isinstance (matt, Passenger)

def test_passengers1():
    name = 'Vanessa Harding'
    passport_no = 74652981

    assert [Passenger.passenger_instances[-3].name, Passenger.passenger_instances[-3].passport_no] == [name, passport_no]

def test_passengers2():
    name = 'Joanna Thompson'
    passport_no = 87235731

    assert [Passenger.passenger_instances[-2].name, Passenger.passenger_instances[-2].passport_no] == [name, passport_no]

def test_passengers3():
    name = 'Burt Kuman'
    passport_no = 78925146

    assert [Passenger.passenger_instances[-1].name, Passenger.passenger_instances[-1].passport_no] == [name, passport_no]

# I get an error if passenger is created without name or passport number
        # Test for it breaking!
def test_passenger_break():
    with pytest.raises(TypeError):
        joe = Passenger()


#-----------Planes--------------
# I can create a plane with a plane number
def test_create_plane():

    jumbo_jet = Plane('Jumbo Jet', 900, 'multi-colour')

    name = 'Jumbo Jet'
    capacity = 900
    colour = 'multi-colour'

    assert [Plane.plane_instances[-1].name, Plane.plane_instances[-1].capacity, Plane.plane_instances[-1].colour] == [name, capacity, colour]



#-----------Flight_trips--------
# I can create a flight with no specific information


# I can add a plane to the flight
# I can add a destination
# I can add an origin
# I can add a passenger to the passengers list
# Passenger list is a list of objects that are passengers

