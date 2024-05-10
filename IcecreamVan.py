# Opgave fra # 11 i Programmering 2. Arv / Inheritance

class Vehicle:                                    # Parent class
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
    def cost(self):
        return self.mileage * 20

class Bus(Vehicle):                               # Child class Bus inherits from parents class Vehicle
    pass

class Van(Vehicle):                               # Child class Van inherits from parents class Vehicle         
    pass


School_bus = Bus("School Volvo", 12, 50)          # object- instance of Child Bus that inherits from Parent class
print("\n Total Bus fare is:", School_bus.fare())

IcecreamVan = Van("Icecream Van", 25, 2)         # object - instance of child Van that inherits from Parent vehicle
print("\n The total cost of today's travel is: ", IcecreamVan.cost())
