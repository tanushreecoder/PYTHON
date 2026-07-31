#A Python program that defines an abstract Animal base class with a shared constructor and an abstract speak() method, then builds three child classes (Dog, Parrot, Lion) that each inherit from Animal using super(), add their own unique attribute, and implement speak() with their own output. Finally, you create objects from each child class and run the sound show.
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    def display(self):
        print(f"Name: {self.name} | Habitat: {self.habitat}")
    @abstractmethod
    def speak(Self):
        pass
class Dog(Animal):
    def __init__(self, name, habitat, breed, phrase):
        super().__init__(name, habitat)
        self.breed = breed
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} ({self.breed}) says {self.phrase}")
class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} lives {self.habitat} says {self.phrase}")
class Lion(Animal):
    def __init__(self, name, habitat, pride, phrase):
        super().__init__(name, habitat)
        self.pride = pride
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} ({self.habitat}) says {self.phrase}")
dog = Dog("Lily", "Home", "Husky", "Woof Woof!")
parrot = Parrot("Polly", "Jungle", "SQUAK")
lion = Lion("Simba", "Savannah", "Pride rock", "ROAR")
print("===Animal sound Show===\n")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()