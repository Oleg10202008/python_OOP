from random import randint

class Student:
    rnd = randint(3, 7)

    def __init__(self, surname="sidorov", age="14", name="lexa", life="normal", happy="60%", proc="30%"):
        self.surname = surname
        self.age = age
        self.name = name
        self.life = 0
        self.happy = 50
        self.proc = True

    def studi(self):
        print("Время учится\n", "=" * 15)
        self.proc += Student.rnd
        self.happy -= Student.rnd

    def sleep(self):
        print("Время спать\n", "=" * 15)
        self.happy += Student.rnd

    def relax(self):
        print("Время отдыха\n", "=" * 15)
        self.proc -= Student.rnd
        self.happy += Student.rnd

    def stud_life(self):
        if self.proc <= 3:
            print("u tebya problemi")
            self.life = False
        elif self.proc >= 4:
            print("tebya reabilitirivali")
            self.life = True

    def every_day(self):
        print("показатель радости", self.happy)
        print("показатель успеваемости", self.proc)

    def resolt(self):
        day = "статистика по студенту " + self.name + self.surname
        print(day)
        print("студент выбирает__________")

        chois = randint(1, 3)

        if chois == 1:
            self.studi()
            print("студент выбрал учиться")

        elif chois == 2:
            self.sleep()
            print("студент выбрал спать")

        else:
            self.relax()
            print("студент выбрал отдых")

stud1 = Student()
num = int(input("введите периодичность: "))
for day in range(num):
    stud1.resolt()