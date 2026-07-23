classroom = [
{
"name": "Omar",
"GPA": 3.5
},
{
"name": "Sara",
"GPA": 3.9
},
{
"name": "Ali",
"GPA": 3.2
}
]

signups = ["Omar", "Sara", "Omar", "Ali", "Sara", "Omar"]
signups = list(set(signups))

print("Mona in signups:", "Mona" in signups)
print("Number of unique signups:", len(signups))
print(signups)

for student in classroom:
    if student["GPA"] >= 3.5:
        print(student["name"], "has a GPA of", student["GPA"])

