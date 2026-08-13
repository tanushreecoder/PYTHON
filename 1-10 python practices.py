#1. Print 'hello world'
print("Hello World")
#2. Write a Python program to do arithmetical operations addition and division.
addordiv = input("Do you want to do? [Addition/Division]: ").lower()
num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
if addordiv == "addition":
    add = num1 + num2
    print(f"After adding {num1} to {num2}, the result is {add}")
elif addordiv == "division":
    div = num1 / num2
    print(f"After dividing {num1} with {num2}, the result is {div}")
else:
    print("Thats not an option!!")
#3. Write a Python program to find the area of a triangle.
base = int(input("Enter base of your triangle: "))
height = int(input("Enter the height of your triangle: "))
area = 0.5 * base * height
print(f"The area of your triangle is: {area}")
#4. Write a Python program to swap two variables
var1 = "abc"
var2 = "lily"
print(f"Variable before swapping; var1 = {var1}; var2 = {var2}")
v3 = var1
v4 = var2
var1 = v4
var2 = v3
print(f"Variable after swapping; var1 = {var1}; var2 = {var2}")
#5. Write a Python program to generate a random number.
import random
print("A random number in 1-1000 is", random.randint(1, 1000))
#6. Write a Python program to convert kilometers to miles.
km = int(input("Enter the number of km: "))
miles = km * 0.621371
print(f"Mile = {miles}")
#7. Write a Python program to convert Celsius to Fahrenheit.
c = int(input("Enter the celcius: "))
f = (c*1.5)+32
print(f"Fahrenheit: {f}")
#8. Write a Python program to display calendar.
import calendar
year = int(input("Enter year: ")) 
month = int(input("Enter month: ")) 
cal = calendar.month(year, month) 
print(cal)
#9. Write a Python program to solve quadratic equation.
#I dont know what is quadratic equation :(
#10. Write a Python program to swap two variables without temp variable.
a = "aba"
b = "bab"
print(f"Before swapping, a = {a}, b = {b}")
a, b = b, a
print(f"After swapping, a = {a}, b = {b}")