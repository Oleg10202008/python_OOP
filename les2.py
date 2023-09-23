from random import *
# class People:

#     def __init__(self,name="vasya"):
#         self.name=name
#
# class Auto:
#     def __init__(self, brend="BMW"):
#         self.brend=brend
#         self.mest=[]
#     def add (self, *args):
#         for i in args:
#             self.mest.append(i)
#
#     def pep_name(self):
#         if self.mest==[]: print("nikogo net v",self.brend)
#         else:
#             print(" imena pasashirov v ",self.brend)
#             for i in self.mest:
#                 print(i.name)
#
#
#
# people1=People()
# people2=People("Katya")
# people3=People("Masha")
# car=Auto()
# car.add(people1,people2,people3)
# car.pep_name()
# car2=Auto("TOYOTA")
# car2.add(people2,people3)

class Human:
    def __init__(self,name="Sasha",job=None,home=None,car=None):
        self.name=name
        self.job=job
        self.home=home
        self.car=car
        self.money=100
        self.happy=50
        self.status=50
    def get_jod(self):
        self.job=job(job_list)
    def get_home(self):
        self.home=home()
    def get_car(self):
        self.car=Auto(auto_list)
    def  eat (self):
        if self.home.food<=0:
            self.shop("produkt")
        else:
            if self.status>=100:
                self.status=100
                return
            self.status+=10
            self.home.food-=10
    def shop(self, sh):
        if sh=="produkt":
            self.money-=50
            self.car.бeнзин-=50

        if sh == "car_produkt":
            self.money -= 80
            self.car.бeнзин -= 50

        if sh == "home_produkt":
            self.money -= 30
            self.car.бeнзин -= 50
            self.happy +=20
    def azs(self):
        if self.car.бeнзин -= 10
            self.money -=20
    def clening(self):
        if self.home.order<=0:
            self.happy -= 20
            self.status -=10
        else:
            self.happy += 20
            self.status += 10

    def days(self,day):
        pass
    def human_stats(self):
        pass
    def live(self):
        pass

class job:
    def  __init__ (self,job_list):
        self.job=choice(list(job_list))
        self.zp=job_list[self.job]["zp"]
        self.hapy_job = job_list[self.job]["hapy_job"]

job_list={
        "Python dev midle":{"zp":5000, "hapy_job":60 },
        "C++ dev senior":{"zp":10000, "hapy_job":90 },
        "Jawa dev junior":{"zp":1800, "hapy_job":50 }
    }

class Auto:
    def  __init__ (self,auto_list):
        self.auto=choice(list(auto_list))
        self.Ts=auto_list[self.auto]["Top speed"]
        self.To = auto_list[self.auto]["Toplivo"]

auto_list={
        "Bmw X5":{"Top speed":280, "Toplivo":"Dizel" },
        "Chevrole Camaro":{"Top speed":320, "Toplivo":"Benzin" },
        "Tesla model 3":{"Top speed":250, "Toplivo":"Electro" }
    }

class home:
    def __init__(self):
        self.food=0
        self.order=0















