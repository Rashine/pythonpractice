class User:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
    def full_name(self):
        return f"{self.name} {self.last}"

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 20)

print (user1.full_name())


class Chicken:
    total_eggs = 0
    def __init__(self, species, name):
        self.eggs = 0
        self.species = species
        self.name = name
    def lay_egg(self):
        self.eggs += 1
        self.total_eggs += 1
        Chicken.total_eggs += 1
        return f"{id(self.eggs)}_{id(self.total_eggs)}_{id(Chicken.total_eggs)}_{self.eggs}_{self.total_eggs}"
        
c1 = Chicken("ccc", "ccc")
print(c1.lay_egg())
c2 = Chicken("ccc", "ccc")
print(c2.lay_egg())
print(c2.lay_egg())
print(c2.lay_egg())
c3 = Chicken("ccc", "ccc")
print(c3.lay_egg())
