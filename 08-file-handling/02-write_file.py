# Write data to a file.

# Writing replaces existing content
with open("sample.txt", "w") as file:
    file.write("Python is fun.\n")
    file.write("Learning by practice is the best way.\n")

print("Content written successfully.")

# Verify the contents
with open("sample.txt", "r") as file:
    print("\nUpdated file:")
    print(file.read())