# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # This method will be overridden by subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Creating instances
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Testing polymorphism
vehicles = [car, plane, boat, bicycle]
for vehicle in vehicles:
    print(vehicle.move())
