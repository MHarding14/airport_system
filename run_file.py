from connect_to_db import *
from passenger_class import *
import pyodbc

#--------------------Load 4 Passengers-----------------------
connect_db = Connect_MS_SQL(server='localhost,1433', database='Airport')

for x in connect_db.pull_passengers():

    rows = list(x)
    Passenger(rows[0], rows[1], rows[2], rows[3])

#---------------------Save Passenger Instance-----------------
charles = Passenger('Charles Hutch', 75629715, 'Male', 24)

connect_db.query(f"INSERT INTO [Passengers] ([PassengerName], [Passport_No], [Gender], [Age]) "
                 f"VALUES ('{charles.name}', '{charles.passport_no}', '{charles.gender}', '{charles.age}')")

connect_db.docker_conn.commit()

print(Passenger.passenger_instances)