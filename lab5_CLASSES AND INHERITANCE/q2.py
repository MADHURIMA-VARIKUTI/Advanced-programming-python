class Vehicle:
    def __init__(self):
        name = input("Enter the name of the vehicle:")
        vehicleidno = int(input("Enter the vehicle id of the vehicle:"))
        manufacturer = input("Enter the manufacturer:")          
        self.name = name
        self.vehicleidno = vehicleidno
        self.manufacturer =manufacturer

class Passenger(Vehicle):
    def __init__(self):
        super().__init__()
        number_of_Passengers = int(input("Enter the number of Passengers:"))
        self.number_of_Passengers = number_of_Passengers
    def display(self):
        print("Name of the Vehicle:",self.name)
        print("Vehicle ID:",self.vehicleidno)
        print("Manufacturer:",self.manufacturer)
        print("Capacity of the Vehicle:",self.number_of_Passengers)
        
passenger1= Passenger()
passenger1.display()

# Enter the name of the vehicle:audi
# Enter the vehicleid of the vehicle:1111
# Enter the manufacturer:man_audi
# Enter the number of Passengers:2
# Name of the Vehicle: audi
# Vehicle ID: 1111
# Manufacturer: man_audi
# Capacity of the Vehicle: 2