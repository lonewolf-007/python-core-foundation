student = {
    "name": "Garvit",
    "course": "BCA",
    "semester": 5
}

print("Student Name:", student["name"])

student["college"] = "PCGE Jaipur"

for key, value in student.items():
    print(key, ":", value)
