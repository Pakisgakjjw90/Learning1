class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("Some generic sound")
    
class Cat(Animal):
    
    def speak(self):
        print(f"{self.name} says Meow!")
    
class Dog(Animal):
    
    
    def speak(self):
        print(f"{self.name} says Woof!")

d1=Dog("Bob")


c1=Cat("Mister_sprinkles")


d2=Dog("Mark")


c2=Cat("Asteroid_destroyer")

Animals=[d1,c1,d2,c2]
for animal in Animals:
    animal.speak()
    
