#First Python Programs
'''
1. Start the code
2. Take input from user
3. Check weather the number is divisible by 2 or not
4. Print the results of weather the number is an odd or even number
'''
n = int(input("Enter your number: "))
if n % 2 == 0:
    print(f"The number {n} is an even number")
else:
    print(f"The number {n} is an odd number")
#Temperature converter
cel = float(input("Enter your temperature in celcius: "))
faranheight = (cel * 9 / 5) + 32
print(f"In faranheight it is {faranheight}")
p = float(input("Enter your principal: "))
r = float(input("Enter your rate: "))
t = float(input("Enter your time: "))
intrest = (p * r * t) / 100
print(f"Your interest is {intrest}")