from random import randint

class Student:
    def __init__(self, surname="Sidorov", age=14, name="Lexa"):
        self.surname = surname
        self.age = age
        self.name = name
        self.life = True
        self.happy = 50
        self.proc = 30
        self.money = 100

    def study(self):
        print("Time to study\n" + "=" * 15)
        self.proc += randint(3, 7)
        self.happy -= randint(1, 3)
        self.money -= randint(5, 15)

    def sleep(self):
        print("Time to sleep\n" + "=" * 15)
        self.happy += randint(1, 5)
        self.money -= randint(1, 5)

    def relax(self):
        print("Time to relax\n" + "=" * 15)
        self.proc -= randint(1, 3)
        self.happy += randint(3, 8)
        self.money -= randint(5, 20)

    def work(self):
        print("Time to work\n" + "=" * 15)
        self.money += randint(20, 50)
        self.happy -= randint(5, 15)

    def student_life(self):
        if self.proc <= 3:
            print("You have academic problems.")
            self.life = False
        elif self.proc >= 4:
            print("You have been rehabilitated.")
            self.life = True

    def every_day(self):
        print("Happiness level:", self.happy)
        print("Academic performance level:", self.proc)
        print("Money:", self.money)

    def run_a_year(self):
        for day in range(365):
            print("\nDay", day + 1)
            self.every_day()

            if not self.life:
                print("Game over! You failed as a student.")
                break

            if self.money <= 0:
                print("You're out of money! Time to work.")
                self.work()

            if self.proc <= 3:
                print("You're failing academically! Time to study.")
                self.study()
            elif self.happy <= 20:
                print("You're not happy! Time to relax.")
                self.relax()
            else:
                choice = randint(1, 4)
                if choice == 1:
                    self.study()
                elif choice == 2:
                    self.sleep()
                elif choice == 3:
                    self.relax()
                else:
                    self.work()

            self.student_life()

        if self.life:
            print("Congratulations! You survived the year as a student.")

# Create a student and run the simulation for a year
stud1 = Student()
stud1.run_a_year()