"""
Author: Aung Zin Paing
This app store the user input on the car and store it in the vehicle super class. Store the attributes and output the data in an understandable format. 
"""
#Super class Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}"

#Automobile class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"{super().__str__()}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"

#Main function
def main():
    vehicle_type = "car"  # Default vehicle type is car
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print(car)


if __name__ == "__main__":
    main()
