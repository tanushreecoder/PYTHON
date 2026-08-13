tup1 = (9, 4, 94, 83, 733, 134)
print(tup1)
students = (
    ("Tanushree", 99), ("Bob", 92), ("Devin", 89), ("Lily", 40)
)
for name, mark in students:
    print(name, mark)
results = sorted(students, key=lambda x:x[1], reverse=True)
print(results)
names = ("Tanushree", "Milly", "David")
marks = (90, 92, 97)
students = tuple(zip(names, marks))
print(students)
def palind(r):
    e = len(r)-1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s += 1
        e -= 1
        return True
r = (1, 2, 3, 3, 2, 1)
if (palind(r)):
    print("The tuple is Flip Flop")
else:
    print("The tuple is not Flip Flop")
weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in range(0, 7):
    if(weather[i]==0):
        rainy += 1
    else:
        sunny += 1
if (sunny>rainy):
    print("Good Weather")
else:
    print("Bad Weather")
