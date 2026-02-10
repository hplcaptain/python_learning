students = {
    "Alice": 85,
    "Mark": 70,
    "David": 65
}

name = input("Enter Student Name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")