class People:

    def __init__(self,name="vasya"):
        self.name=name

class Auto:
    def __init__(self, brend="BMW"):
        self.brend=brend
        self.mest=[]
    def add (self, *args):
        for i in args:
            self.mest.append(i)

    def pep_name(self):
        if self.mest==[]: print("nikogo net v",self.brend)
        else:
            print(" imena pasashirov v ",self.brend)
            for i in self.mest:
                print(i.name)



people1=People()
people2=People("Katya")
people3=People("Masha")
car=Auto()
car.add(people1,people2,people3)
car.pep_name()
car2=Auto("TOYOTA")
car2.add(people2,people3)