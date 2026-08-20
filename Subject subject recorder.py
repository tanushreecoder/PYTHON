students = {
    "S001": {"name": "Alice", "subject": "Python", "marks": 85},
    "S002": {"name": "Bob", "subject": "Math", "marks": 78},
    "S003": {"name": "Charlie", "subject": "English", "marks": 92},
    "S004": {"name": "David", "subject": "Python", "marks": 85},
    "S005": {"name": "Alice", "subject": "Python", "marks": 85}  # duplicate
}
print("Original Records:")
print(students)
print("\nAccessing Records Safely:")
record = students.get("S002")
if record:
    print("S002:", record)
else:
    print("Student not found")
students["S006"] = {
    "name": "Emma",
    "subject": "Science",
    "marks": 88
}
students["S002"]["marks"] = 82
students.pop("S004", None)
unique_records = {}
for student_id, record in students.items():
    record_key = (record["name"], record["subject"], record["marks"])
    if record_key not in unique_records:
        unique_records[record_key] = (student_id, record)
students = {
    student_id: record
    for student_id, record in unique_records.values()
}
print("\nNumber of Final Records:", len(students))
print("\nFinal Student Records:")
for student_id, record in students.items():
    print(
        f"ID: {student_id}, "
        f"Name: {record['name']}, "
        f"Subject: {record['subject']}, "
        f"Marks: {record['marks']}"
    )
