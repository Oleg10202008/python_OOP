class Student():
    print("hi student")
    kol=0
    def __init__(self,name,age,surname):
        self.name=name
        self.age=age
        self.surname=surname
        Student.kol+=1
    def inf(self):
        print(self.name,self.age,self.surname)

stud1=Student("oleg","14","Sushko")
print(stud1.name)
print(stud1.age)
print(stud1.surname)
print("\n")
stud2=Student("ana","17","str")
print(stud2.name)
print(stud2.age)
print(stud2.surname)
print("\n")

print(Student.kol)