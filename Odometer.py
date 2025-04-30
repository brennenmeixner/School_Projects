# Defined class
class Odometer:
    def __init__(self):
        self.miles = 0
        self.fuel_efficiency = 0  # miles per gallon

    def reset(self):
        self.miles = 0

    def set_fuel_efficiency(self, mpg):
        self.fuel_efficiency = mpg

    def add_miles(self, trip_miles):
        self.miles += trip_miles

    def get_gallons_consumed(self):
        if self.fuel_efficiency == 0:
            return 0
        return self.miles / self.fuel_efficiency


# test program
car = Odometer()

car.set_fuel_efficiency(25)
car.add_miles(100)
print("Trip 1: gallons consumed:", car.get_gallons_consumed())

car.reset()
car.set_fuel_efficiency(30)
car.add_miles(150)
print("Trip 2: gallons consumed:", car.get_gallons_consumed())

car.reset()
car.set_fuel_efficiency(20)
car.add_miles(60)
print("Trip 3: gallons consumed:", car.get_gallons_consumed())
