# ============================================================
# Name:        Vehicle and Automobile Program
# Author:      [Your Name]
# Date:        [Date]
# Description: This program uses inheritance to create a
#              Vehicle superclass and an Automobile subclass.
#              The program collects information about a car
#              from the user and displays the information.
# ============================================================


# Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        # Store the type of vehicle
        self.vehicle_type = vehicle_type


# Automobile subclass inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Call the Vehicle superclass constructor
        super().__init__(vehicle_type)

        # Store automobile information
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# ------------------------------------------------------------
# Get information about the car from the user
# ------------------------------------------------------------

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")


# Create an Automobile object.
# The vehicle type is automatically set to "car".
car = Automobile("car", year, make, model, doors, roof)


# ------------------------------------------------------------
# Display the vehicle information
# ------------------------------------------------------------

print("\nVehicle Information")
print("-------------------")
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)