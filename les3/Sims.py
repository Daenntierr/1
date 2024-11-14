import random
import logging

logging.basicConfig(filename='simulation.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 10
        self.job = job
        self.car = car
        self.home = home
        logging.info(f'{self.name} has been created with initial money={self.money}, gladness={self.gladness}, satiety={self.satiety}')

    def get_home(self):
        self.home = House()
        logging.info(f'{self.name} has acquired a new house.')

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f'{self.name} has bought a {self.car.brand} car.')

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
            logging.info(f'{self.name} has found a job as a {self.job.job} with salary {self.job.salary}.')
        else:
            self.to_repair()
            logging.info(f'{self.name} needs to repair the car before getting a job.')

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                logging.info(f'{self.name} is already full.')
                return
        self.satiety += 5
        self.home.food -= 5
        logging.info(f'{self.name} ate food. Satiety is now {self.satiety}.')

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
            logging.info(f'{self.name} worked as a {self.job.job}. Earned {self.job.salary} money, satiety is now {self.satiety}, gladness is now {self.gladness}.')
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
                logging.info(f'{self.name} needs to repair the car before working.')

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.money -= 100
            self.car.fuel += 100
            logging.info(f'{self.name} bought fuel. Remaining money: {self.money}, fuel: {self.car.fuel}')
        elif manage == "food":
            self.money -= 50
            self.home.food += 50
            logging.info(f'{self.name} bought food. Remaining money: {self.money}, food in house: {self.home.food}')
        elif manage == "delicacies":
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
            logging.info(f'{self.name} bought delicacies. Gladness: {self.gladness}, satiety: {self.satiety}, remaining money: {self.money}')

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f'{self.name} is chilling. Gladness is now {self.gladness}, mess in house is {self.home.mess}.')

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f'{self.name} cleaned the house. Gladness is now {self.gladness}, mess in house is {self.home.mess}.')

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f'{self.name} repaired the car. Car strength is now {self.car.strength}, remaining money: {self.money}.')

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f'{self.name} has depression…')
            return False
        if self.satiety < 0:
            logging.warning(f'{self.name} has died due to hunger…')
            return False
        if self.money < -500:
            logging.warning(f'{self.name} has gone bankrupt…')
            return False

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
            logging.info(f'{self.name} settled in the house.')
        if self.car is None:
            self.get_car()
            logging.info(f'{self.name} bought a car {self.car.brand}.')
        if self.job is None:
            self.get_job()
            logging.info(f'{self.name} got a job {self.job.job}.')
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            logging.warning(f'The car {self.brand} cannot move. Fuel: {self.fuel}, Strength: {self.strength}')
            return False


class House:
    def __init__(self):
        self.mess = 10
        self.food = 10


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break
