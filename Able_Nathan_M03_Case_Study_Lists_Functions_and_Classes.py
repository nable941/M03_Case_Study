"""
Nathan Able
M03 Case Study
This program has two classes has two classes in which the Vehicle class is independent
and the Automobile class inherits the Vehicle class

"""

#Define parent class
class Vehicle:
    #initalize attributes of class
    def __init__(self, vehicleType) -> None:
            self.vehicleType = vehicleType

#Define child class
class Automobile(Vehicle):
    #Initialize attributes of child class with the inherited parent attributes
    def __init__(self, vehicleType, year, make, model, doors, roof) -> None:
        #use paerent class to manage its own attributes
         super().__init__(vehicleType)
         self.year = year
         self.make = make
         self.model = model
         self.doors = doors
         self.roof = roof

#create object 
vehType = Vehicle(input("Enter your vehicle type (car, truck, bus, etc.)? "))

#assign attributes to varibles
vehYear = input("What is the "+ vehType.vehicleType + " year? ")
vehMake = input("what is the " + vehType.vehicleType + " make? ")
vehModel = input("What is the " + vehType.vehicleType + " model? ")
vehDoors = input("Does the " + vehType.vehicleType + " have 2 or 4 doors? ")
vehRoof = input("Does the " + vehType.vehicleType + " have a solid or sun roof? ")

#create car object using vehicle object and variable data
car = Automobile(vehType.vehicleType, vehYear, vehMake, vehModel, vehDoors, vehRoof)

#print results   
print("You entered:")
print("Vehicle Type: " + car.vehicleType)
print("Year: " + car.year)
print("Make: " + car.make)
print("Model: " + car.model)
print("Doors: " + car.doors)
print("Roof: " + car.roof)



