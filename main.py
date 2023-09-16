from random import randint


# class Student():
#     print("hi student")
#     kol=0
#     def __init__(self,name,age,surname):
#         self.name=name
#         self.age=age
#         self.surname=surname
#         Student.kol+=1
#     def inf(self):
#         print(self.name,self.age,self.surname)
#
# stud1=Student("oleg","14","Sushko")
# print(stud1.name)
# print(stud1.age)
# print(stud1.surname)
# print("\n")
# stud2=Student("ana","17","str")
# print(stud2.name)
# print(stud2.age)
# print(stud2.surname)
# print("\n")
#
# print(Student.kol)

class Student:
    rnd = randint(3, 7)
    def __init__(self,surname="sidorov",age="14",name="lexa",life="normal",happy="60%",proc="30%"):
        self.surname=surname
        self.age=age
        self.name=name
        self.life=0
        self.happy=50
        self.proc=True

    def studi(self):
        print("Время учитса\n","="*15)
        self.proc+=Student.rnd
        self.happy-=Student.rnd
    def sleep(self):
        print("Время спать\n","="*15)
        self.happy+=Student.rnd
    def relax(self):
        print("Время отдыха\n","="*15)
        self.proc-=Student.rnd
        self.happy+=Student.rnd

    def stud_life(self):
        if self.proc<=3:
            print("u tebya problemi")
            self.life=False
        elif self.proc>=4:
            print("tebya reabilitirivali")
            self.life = True

    def every_day(self):
        print("показатель радости",self.happy)
        print("показатель успиваемости", self.proc)

    def resolt(self):
        day =""+" статистика по студенту "+ self.name+self.surname
        print(day)
        print("студент вибирает__________")

        chois=randint(1,3)

        if chois == 1:
            self.studi()
            print("студент вибрал учится")

        elif chois ==2:
            self.sleep()
            print("студент вибрал спать")

        else:
            self.relax()
            print("студент вибрал отдих")

stud1= Student()
num=int(input("введите переодичность"))
for day in range(num):
    stud1.resolt(day)
























