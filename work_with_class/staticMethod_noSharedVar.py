class abc:
    def __init__(self, a=0):
        self.a = a
        self.b = None

    @classmethod
    def from_const(cls, b=30):
        self = cls(10)
        self.b = b
        return self

    def printme(self):
        print(self.a,self.b)


a1 = abc(a=100)
a2 = abc.from_const(b=31)
a3 = abc.from_const(b=41)
a4 = abc().from_const(b=51)
a5 = abc().from_const(b=61)


a1.printme()
a2.printme()
a3.printme()
a4.printme()
a5.printme()
