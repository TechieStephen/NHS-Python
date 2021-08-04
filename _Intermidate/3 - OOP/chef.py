class Chef:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def chefDetails(self):
        print("Chef Details")
        print("Name: " + self.name)
        print("Age: " + str(self.age))

    def makeBurger(self):
        print("COOKING..............BURGER IS READY")

    def makeRice(self):
        print("COOKING..............RICE IS READY")


class NigerianChef(Chef):
    def __init__(self, tribe, name, age, gender):
        Chef.__init__(self, name, age, gender)
    
    def makeJollof(self):
        print("COOKING..............JOLLOF IS READY")


sam = NigerianChef('Igbo','sam', 78, 'male')
sam.makeBurger()
sam.makeRice()
sam.makeJollof()

sun = Chef('sun', 45, 'female')
sun.makeBurger()
sun.makeRice()