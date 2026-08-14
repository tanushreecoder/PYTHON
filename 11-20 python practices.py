#11. Write a Python Program to Check if a Number is Positive, Negative or Zero.
n = int(input("Enter your number: "))
if n > 0:
    print(f"{n} is a positive number")
elif n < 0:
    print(f" is a negative number")
else:
    print(f"{n} is 0 or a newtral number")
#12. Write a Python Program to Check if a Number is Odd or Even.
n = int(input("Enter your number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
#13. Write a Python Program to Check Leap Year.
y = int(input("Enter the year to check if its a leap year: "))
if y % 4 == 0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")
#14. Write a Python Program to Check Prime Number.
num = int(input("Enter a number: "))
f = False
if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            f = True
            break
if f:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
#15. Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
l = int(input("Input a number: "))
u = int(input("Input a number larger than the next: "))
print(f"Prime numbers between {l} and {u} are:")
if l < u:
    for num in range(l, u + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
else:
    print("Error")
#16. Write a Python Program to Find the Factorial of a Number.
num - int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial numbers do exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")
#17. Write a Python Program to Display the multiplication Table.
num = int(input("The mulitplication table of: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
#18. Fibonacci Sereies
terms = int(input("How many terms: "))
n1 = 1
n2 = 0
count = 0
if terms <=0:
    print("Enter a positive number")
elif terms > 1:
    print(f"Fibonacci series up to: {terms} terms: ")
    while count<terms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1