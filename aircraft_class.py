class Aircraft:

    def __init__(self):
        self.working = True
        self.passenger_aircraft = True

    def fly(self):
        return('Wooooow.. look how high I am!!')

    def take_off(self):
        return("Hold on.. we're about to go up!!")

    def land(self):
        return('Hold on.. this could get bumpy!!')

    def taxi(self):
        return("Wait a minute... we'll be on the way soon!!")


# tornado = Aircraft('green')
#
# print(tornado.taxi())
# print(tornado.take_off())
# print(tornado.fly())
# print(tornado.land())