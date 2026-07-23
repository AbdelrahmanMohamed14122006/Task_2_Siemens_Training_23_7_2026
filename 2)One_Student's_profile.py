student = {
"name": "Sara",
"age": 22,
"GPA": 3.1,
"City": "Cairo"
}

del student["age"]
student["GPA"] = 3.6
student["City"] = "Giza"

for key in student:
    print(key, ":", student[key])

print(student)