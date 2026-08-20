habits = {
    "Study": [1, 1, 0, 1, 1, 0, 1],
    "Exercise": [0, 1, 1, 0, 1, 0, 1],
    "Read": [1, 1, 0, 0, 1, 1, 1],
    "Drink Water": [1, 1, 1, 1, 1, 1, 1]
}
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("WEEKLY HABIT TRACKER")
for habit in habits:
    print(habit + ":")
    for i in range(7):
        if habits[habit][i] == 1:
            print(days[i], "- Done")
        else:
            print(days[i], "- Not Done")
    total = 0
    for value in habits[habit]:
        if value == 1:
            total += 1
    print("Completed:", total, "out of 7 days")
    print()
