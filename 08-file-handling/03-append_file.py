# Append data without removing the existing content.

with open("sample.txt", "a") as file:
    file.write("Keep practicing every day.\n")

print("New content appended.")

# Display the updated file
with open("sample.txt", "r") as file:
    print("\nCurrent file content:")
    print(file.read())