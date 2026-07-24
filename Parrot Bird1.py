#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Lemon = Parrot("Lemon", 2)
Momo = Parrot("Momo", 1)
print(f"Lemon is a {Lemon.species}")
print(f"Momo is also a {Momo.species}")
print(f"Lemon is {Lemon.age} years old")
print(f"Momo is {Momo.age} years old")