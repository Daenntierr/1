import random
from tkinter.font import names


class Dog:
    def __init__(self, name , dog_name="Barca"):
        self.name = name
        self.dog_name = dog_name
        self.gladness = 50
        self.progress = 50
        self.money = 10
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 2
        self.progress -= 0.4
        self.money -= 2

    def to_work(self):
        print("Time to work")
        self.progress += 0.3
        self.gladness -= 0.3
        self.money += 2


    def is_alive(self):
        if self.progress < -0.5:
            print("Ohhh crap!")
            self.alive = False
        elif self.gladness <= 0:
            print("Sad")
            self.alive = False
        elif self.progress > 10:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("Cash out,I need to work harder!")
            self.alive = False

    def end_of_day(self):

        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):

        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_work()
        elif live_cube == 4:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

name = input("What is your name? ")
barca = Dog(name="Barca")
print(barca.dog_name)
for day in range(365):
    if barca.alive == False:
        break
    barca.live(day)