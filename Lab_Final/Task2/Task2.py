# Task 2 - Student Ranking (Manual Sorting)

class Student:
    def __init__(self, id, mark):
        self.id = id
        self.mark = mark


def comes_before(a, b):
    # higher mark first
    if a.mark > b.mark:
        return True
    # if tie, smaller ID first
    if a.mark == b.mark and a.id < b.id:
        return True
    return False


# 📥 Step 1: Read input
with open("input2.txt") as f:
    n = int(f.readline())
    ids = list(map(int, f.readline().split()))
    marks = list(map(int, f.readline().split()))


# 🧱 Step 2: Create objects
students = []
for i in range(n):
    students.append(Student(ids[i], marks[i]))


# 🔁 Step 3: Selection sort
for i in range(n):
    best = i
    for j in range(i + 1, n):
        if comes_before(students[j], students[best]):
            best = j

    students[i], students[best] = students[best], students[i]


# 💾 Step 4: Write output
with open("output2.txt", "w") as f:
    for s in students:
        f.write(f"ID: {s.id} Mark: {s.mark}\n")