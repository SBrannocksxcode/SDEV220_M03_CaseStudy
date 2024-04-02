class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle Information:")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def main():
    print("Welcome to the Automobile Information App!")
    
    automobile = Automobile()
    automobile.set_vehicle_type("car")

    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    automobile.set_attributes(year, make, model, doors, roof)
    automobile.display_info()


if __name__ == "__main__":
    main()