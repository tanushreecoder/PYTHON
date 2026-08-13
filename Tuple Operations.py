tup1 = (9, 4, 94, 83, 733, 134)
print(tup1)
students = (
    ("Tanushree", 99), ("Bob", 92), ("Devin", 89), ("Lily", 40)
)
for name, mark in students:
    print(name, mark)
results = sorted(students, key=lambda x:x[1], reverse=True)
print(results)