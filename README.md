# Task_2_Siemens_Training_23_7_2026
Python fundamentals: lists &amp; dictionaries in action. Manage a class roster, build a student profile, then combine both into a full classroom with duplicate signups cleaned via set(). Covers append/remove, updates, del, membership checks &amp; GPA filtering. No shortcuts, just core logic


# Software Fundamentals : Lists & Dictionaries

Three small Python programs that practice core `list` and `dict` operations — adding, removing, updating, looping, and deduplicating data.

Each script is self-contained and can be run directly with `python3 <filename>.py`.

---

## 1. The Class List — `1_The_Class_List.py`

Practices basic list operations on a roster of students.

**What it does:**
- Starts with a list of students: `["Omar", "Sara", "Ali", "Nour"]`.
- Adds a new student with `.append("Youssef")`.
- Removes a student with `.remove("Ali")`.
- Prints the total number of students, the first student, and the last student (using index `-1`).
- Loops through the final list and prints every name.

---

## 2. One Student's Profile — `2_One_Student_s_profile.py`

Practices basic dictionary operations on a single student's record.

**What it does:**
- Starts with a dictionary holding one student's `name`, `age`, `GPA`, and `City`.
- Deletes the `age` key entirely with `del`.
- Updates the `GPA` and `City` values.
- Loops through the dictionary's keys, printing each key alongside its value.
- Prints the final dictionary as a whole.

---

## 3. The Whole Class + Remove Duplicates — `3_The_Whole_Class_Remove_Duplicates.py`

Combines a list of dictionaries with duplicate removal and filtering.

**What it does:**
- Stores a `classroom` list, where each entry is a dictionary with a student's `name` and `GPA`.
- Stores a separate `signups` list containing repeated names (simulating multiple sign-up entries).
- Removes duplicates from `signups` using `list(set(signups))`.
- Checks whether `"Mona"` is among the signups.
- Prints how many unique students signed up, and the deduplicated list itself.
- Loops through `classroom` and prints only the students with a GPA of 3.5 or higher.

---

## Concepts covered

- List methods: `.append()`, `.remove()`, indexing (`[0]`, `[-1]`), `len()`
- Dictionary operations: adding/updating keys, `del`, looping over keys
- Combining lists and dictionaries (a list of dictionaries)
- Removing duplicates with `set()`
- Membership testing with `in`
- Filtering data with conditional loops
