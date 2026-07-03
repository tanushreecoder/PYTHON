def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
num = input("Enter your number: ")
if num == 0:
    print("The factorial of 0 is 0")
elif num < 0:
    print("Negative factorials do not exist")
else:
    print(f"The factorial of {num} is {factorial(num)}")