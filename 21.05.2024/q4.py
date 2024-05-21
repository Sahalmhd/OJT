#ElectricCar Class Inheriting from Car Class

class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Car(Vehicle):
    def __init__(self, name, seating_capacity, max_speed):
        super().__init__(name, seating_capacity)
        self.max_speed = max_speed

    def car_info(self):
        return f"{self.name} can seat {self.seating_capacity} people and has a max speed of {self.max_speed} km/h."

class ElectricCar(Car):
    def __init__(self, name, seating_capacity, max_speed, battery_capacity):
        super().__init__(name, seating_capacity, max_speed)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        return f"The battery capacity of {self.name} is {self.battery_capacity} kWh."

electric_car = ElectricCar("Tesla Model 3", 5, 250, 75)
print(electric_car.car_info())
print(electric_car.battery_info())