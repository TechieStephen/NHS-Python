class Animal:
    def __init__(self, name, no_legs):
        self.name = name
        self.no_legs = no_legs

    def animal_sound(self):
        print('the animal made a sound')

class Dog(Animal):
    def __init__(self, name, no_legs, sound):
        Animal.__init__(self, name, no_legs)
        self.sound = sound

    def eat(self):
        print('The dog is eating a bone')

class Cat(Animal):
    def __init__(self, name, no_legs):
        super().__init__(name, no_legs,)

dog1 = Dog('Bingo', 4, 35)
dog1.animal_sound()
dog1.eat()
print(dog1.age)

cat1 = Cat('fgfg', 4)
