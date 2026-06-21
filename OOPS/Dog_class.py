class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def bark(self):
        print(f"{self.name} says woof!")


d1=Dog("Jack","German Shepherd")
d2=Dog("Bob","Husky")
d3=Dog("King","Golden retriever")

d1.bark()
d2.bark()
d3.bark()