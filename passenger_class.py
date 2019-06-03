class Passenger:

    passenger_instances = []

    def __init__(self, name, passport_no, gender = 0, age = 0):
        Passenger.passenger_instances.append(self)
        self.name = name
        self.passport_no = passport_no
        self.gender = gender
        self.age = int(age)
