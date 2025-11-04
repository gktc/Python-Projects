class Animal:
    def __init__(self):
        self.eyes = 2
    
    def breathe(self):
        print("Inhale.... Exhale.....")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in the water")

    def breathe(self):
        super().breathe()
        print("Fish breathing ....")

# Just a demonstration of the inheritance super() and how inheritance is used...
fish  = Fish()
animal = Animal()
print(fish.eyes)


