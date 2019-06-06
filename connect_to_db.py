import pyodbc

class Connect_MS_SQL:

    def __init__(self, server='localhost,1433', database='Northwind', username='SA', password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
        self.cursor = self.docker_conn.cursor()

    def query(self, sql_query):

        return self.cursor.execute(sql_query)

    def pull_passengers(self):

        query = self.query("SELECT * FROM Passengers")
        return query

    def create_passengers(self, name, passport_no, gender, age):

        self.query(f"INSERT INTO Passengers (PassengerName, Passport_No, Gender, Age)"
                            f"VALUES {name}, {passport_no}, {gender}, {age})")


