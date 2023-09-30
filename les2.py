from random import choice

class Human:
    def __init__(self, name="Sasha", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.happy = 50
        self.status = 50

    def get_job(self, job_list):
        self.job = Job(choice(list(job_list)))

    def get_home(self):
        self.home = Home()

    def get_auto(self, auto_list):
        self.car = Auto(choice(list(auto_list)))

    def eat(self):
        if self.home.food <= 0:
            self.shop("produkt")
        else:
            if self.status >= 100:
                self.status = 100
            else:
                self.status += 10
            self.home.food -= 10

    def shop(self, sh):
        if sh == "produkt":
            self.money -= 50
            self.car.consume_fuel(50)

        if sh == "car_produkt":
            self.money -= 80
            self.car.consume_fuel(50)

        if sh == "home_produkt":
            self.money -= 30
            self.car.consume_fuel(50)
            self.happy += 20

    def azs(self):
        if self.car.consume_fuel(10):
            self.money -= 20

    def cleaning(self):
        if self.home.order <= 0:
            self.happy -= 20
            self.status -= 10
        else:
            self.happy += 20
            self.status += 10

    def days(self, day):

        self.eat()
        self.azs()
        self.cleaning()
        self.live(self.happy)

    def human_stats(self):

        return {
            "Name": self.name,
            "Job": self.job.job if self.job else "Unemployed",
            "Home": self.home.__dict__ if self.home else "Homeless",
            "Car": self.car.__dict__ if self.car else "Carless",
            "Money": self.money,
            "Happiness": self.happy,
            "Status": self.status,
        }

    def live(self, Hp):
        if Hp < 50:
            self.happy -= 20
            self.status -= 10
            self.money -= 10

class Job:
    def __init__(self, job):
        self.job = job
        self.zp = job_list[self.job]["zp"]
        self.happy_job = job_list[self.job]["hapy_job"]

class Auto:
    def __init__(self, auto):
        self.auto = auto
        self.Ts = auto_list[self.auto]["Top speed"]
        self.Toplivo = auto_list[self.auto]["Toplivo"]

    def consume_fuel(self, amount):

        if self.Toplivo == "Dizel" or self.Toplivo == "Benzin":
            return True
        return False

class Home:
    def __init__(self):
        self.food = 100
        self.order = 10



if __name__ == "__main__":

    human = Human()


    for day in range(1, 11):
        human.days(day)
        print(f"Day {day}: {human.human_stats()}")

job_list = {
    "Python dev midle": {"zp": 5000, "hapy_job": 60},
    "C++ dev senior": {"zp": 10000, "hapy_job": 90},
    "Jawa dev junior": {"zp": 1800, "hapy_job": 50}
}

auto_list = {
    "Bmw X5": {"Top speed": 280, "Toplivo": "Dizel"},
    "Chevrole Camaro": {"Top speed": 280, "Toplivo": "Benzin"},
    "Tesla model 3": {"Top speed": 250, "Toplivo": "Electro"}
}















