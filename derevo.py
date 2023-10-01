from random import randint, choice

class Tree:
    def __init__(self, age=0, color="Green", height=200, name="Dub"):
        self.age = age
        self.color = color
        self.height = height
        self.name = name

    def every_day(self):
        self.age += 1
        self.height += randint(5, 10)
        print("Age:", self.age)
        print("Height:", self.height)
        print("Color:", self.color)

    def run_a_month(self):
        for day in range(30):
            print("\nDay", day + 1)
            self.every_day()

class Fruti_Tree(Tree):
    def __init__(self, age=0, color="Yellow", height=150, name="Plodovoe", plod="apple"):
        super().__init__(age, color, height, name)
        self.plod = plod

    def fruit_every_day(self):
        self.age += 1
        self.height += randint(3, 7)
        self.plod = choice(plod_list)
        print("Age:", self.age)
        print("Height:", self.height)
        print("Color:", self.color)
        print("Name:", self.name)
        print("Fruit:", self.plod)

    def fruit_run_a_month(self):
        for day in range(30):
            print("\nDay", day + 1)
            self.fruit_every_day()

plod_list = ["apple", "plum", "pear"]

tree = Tree()
tree.run_a_month()

fruit_tree = Fruti_Tree()
fruit_tree.fruit_run_a_month()








