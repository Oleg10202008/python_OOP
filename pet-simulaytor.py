from random import randint

class Cat:

    rnd = randint(3, 7)
    rnd1 = randint(7, 15)
    rnd2 = randint(15, 30)

    def __init__(self, name="barsik", age=5, happy=50, hp=100, golod=0):
        self.name = name
        self.age = age
        self.hp = hp
        self.happy = happy
        self.golod = golod

    def eating(self):
        print("Кушать:")
        self.hp += Cat.rnd
        self.happy += Cat.rnd
        self.golod -= Cat.rnd2

    def playing(self):
        print("Играть:")
        self.hp -= Cat.rnd
        self.happy += Cat.rnd2
        self.golod += Cat.rnd1

    def sleeping(self):
        print("Спать:")
        self.hp += Cat.rnd1
        self.happy += Cat.rnd1
        self.golod += Cat.rnd1

    def cat_life(self):
        if self.hp <= 0 or self.golod >= 100:
            return True
        else:
            return False

    def every_day(self):
        print("Показатель радости:", self.happy)
        print("Показатель жизни:", self.hp)
        print("Показатель голода:", self.golod)

    def resolt(self):
        day = "Cat statistics for " + self.name
        print(day)
        print("__________")

        choice = randint(1, 3)

        if choice == 1:
            self.eating()
            print("Кот выбрал есть")

        elif choice == 2:
            self.sleeping()
            print("Кот выбрал спать")

        else:
            self.playing()
            print("Кот выбрал играть")

cat = Cat()
num = int(input("Введите периодичность: "))
for day in range(num):
    cat.resolt()
    cat.every_day()
    if cat.cat_life():
        print("Кот умер :(")
        break