class Grant:
    def __init__(self,age=50,heir=100,seler=2000):
        self.age=age
        self.heir =heir
        self.seler = seler
    def infG(self):
        print(self.age)
class Parents(Grant):
    def __init__(self, age=30,heir=200,seler=3000):
        super().__init__(age,heir,seler)
    def infP(self):
        print(self.age)
class Sun(Grant):
    def __init__(self, age=15, heir=40, seler=0, studi="yes"):
        super().__init__(age, heir, seler)
        self.studi=studi
    def infS(self):
        print(self.age)

gr=Grant()
gr.infG()
pr=Parents()
pr.infP()
sn=Sun()
sn.infS()


