students = {
    "id1": {"Name": "Sara", "Class": 7, "Expert in subj": "English"},
    "id2": {"Name": "Maher", "Class": 7, "Expert in subj": "Math"},
    "id3": {"Name": "Lily", "Class": 7, "Expert in subj": "Drawing"},
}
result = {}
seen_keys = []
for student_id, details in students.items():
    unique_key = (details["Name"], details["Class"], details["Expert in subj"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
    print(k, ":", v)