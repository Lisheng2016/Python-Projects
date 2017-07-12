class Car():
    def __init__(self,brand):
        if brand != "":
            self.brand = brand
        self.owner = 'Master Jim'
        print "Car initializing completed"

    def turn(self,direction):
        print "Turning %s direction!" % direction


    def accel(self,speed):
        print "This car is speeding up fast!"

    def stop(self):
        print "stop"

class RaceCar(Car):
    def __init__(self,color):
        self.color = color

    def accel(self,speed):
        self.name = "My car"
        print "This is a race car and can speed up to %s very very fast" % speed
car1 = RaceCar('red')

print vars(car1)
print dir(car1.__init__)