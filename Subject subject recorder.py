students = {
    "2001": {"Name": "Sara", "Class": 7, "Expert in subj": "English", "Marks": 82},
    "2002": {"Name": "Maher", "Class": 7, "Expert in subj": "Math", "Marks": 99},
    "2003": {"Name": "Lily", "Class": 7, "Expert in subj": "Drawing", "Marks": 97},
}
print("Original records:")
print(students)
print("Accessing records safely")
records = students.get("2004")
if records:
    print("2004: ", records)
else:
    print("2004 not found")
students[2004] = {"Name": "Simmy", "Class": 7, "Expert in subj": "BGS", "Marks": 97}
students["2004"]["marks"] = 82
students.pop("2004", None)
uniquerecords = {}
for student_items, record in students.item():
    (records["Name"], )