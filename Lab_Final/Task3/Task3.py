# Task3.py

with open("input3.txt") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    m = int(f.readline())
    b = list(map(int, f.readline().split()))

i = j = 0
result = []

while i < n and j < m:
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

with open("output3.txt", "w") as f:
    f.write(" ".join(map(str, result)))