#Bus Class Inheriting from Vehicle Class

class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare

bus = Bus("City Bus", 50)
print(f"Total Bus Fare: {bus.fare()}")
