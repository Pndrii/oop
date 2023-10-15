class Empty:
    pass
class Animal:
    name = str
    mass = float
    def __init__(self, n, m):
        self.name = n
        self.mass = m
    def __str__(self):
        return f"{self.name}({self.mass} kg)"
cat = Animal("Murchyk", 2.8)
print(cat)
