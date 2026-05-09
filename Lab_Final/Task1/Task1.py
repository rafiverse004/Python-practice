# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# Main Code
with open("input1.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

bubble_sort(arr)

with open("output1.txt", "w") as f:
    f.write(" ".join(map(str, arr)))