class Vehicle:
    serial = ""
    license = ""
    def turnonAirCon(self):
        print("Turn on Air")

class Car(Vehicle):
    def sayhello(self):
        print("Hello WOrld")

class Van(Vehicle):
    def saybye(self):
        print("Good Bye")

class Pickup:
    serial = ""
    license = ""
    def turnonAirCon(self):
        print("Turn on Air")


pickup1 = Pickup()
pickup1.turnonAirCon()

car1 = Car()
car1.turnonAirCon()
car1.sayhello()

van1 = Van()
van1.turnonAirCon()
van1.saybye()


