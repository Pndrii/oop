class Priamokutnyk:
    number = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.P = 2*(a+b)
        Priamokutnyk.number += 1
    def opys(self):
        print("прямокуник з периметром", self.P)
A = Priamokutnyk(5, 6)
A.opys()
B = Priamokutnyk(2, 3)
B.opys()
print(Priamokutnyk.number)
