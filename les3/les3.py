from zipapp import create_archive


class Human:

    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def app_passenger(self, * args):
        for passenger in args:
           self.passengers.append(passenger)

    def print_passenger_names(self):
        if self.passengers != []:
            print("Names of", self.brand, "passengers")
            for passengers in self.passengers:
                print(passengers)
        else:
            print("No passengers")

class Passenger:
    def __init__(self, name="Passenger"):
        self.name = name

man1 = Human(name="Jack")
man2 = Passenger(name="Nik")
car = Auto("BMW")
car.app_passenger(man1, man2)
car.print_passenger_names()
