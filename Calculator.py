def addition():
    return a + b
def subtraction():
    return a - b
def multiplication():
    return a * b
def division():
    return a / b
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = input("What do you want to do with those numbers? (Options: Addition/Subtaction/Multiplication/Division): ").lower()
if c == "division":
    print(f"Result =" divition())
elif c == "multiplication":
    print(f"Result =" multiplication())
elif c == "subtaction":
    print(f"Result =" subtaction())
elif c == "addition":
    print(f"Result =" addition())
else:
    print("Try another option")