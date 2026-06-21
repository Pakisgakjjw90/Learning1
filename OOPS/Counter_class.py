class Counter:
    def __init__(self):
        self.count=0
    
    def increment(self):
        self.count+=1
    
    def decrement(self):
        self.count-=1
    
    def reset(self):
        self.count=0
    
    def return_count(self):
        return self.count

c1=Counter()
c1.increment()
c1.increment()
c1.increment()

c1.decrement()
print("The count at this moment is:",c1.return_count())

c1.reset()

print("The count at this moment is:",c1.return_count())

        