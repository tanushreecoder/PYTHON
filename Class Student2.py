#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them
class Student:
    grade = 1
    name = "Snowy"
    def introduction(self):
        print("Hi Im a student")
    def details(self):
        print("Hi my name is ", self.name)
        print("Hi my grade is ", self.grade)
ob = Student()
ob.introduction()
ob.details()