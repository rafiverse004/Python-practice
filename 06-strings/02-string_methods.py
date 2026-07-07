# String methods perform common text operations.

text = "  learn Python Programming  "

# Change letter case
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# Remove whitespace
clean_text = text.strip()
print(clean_text)

# Replace text
print(clean_text.replace("Python", "Java"))

# Find text
print(clean_text.find("Python"))

# Count occurrences
print(clean_text.count("a"))

# Starts and ends with
print(clean_text.startswith("learn"))
print(clean_text.endswith("Programming"))

# Split into a list
words = clean_text.split()
print(words)

# Join a list into a string
sentence = "-".join(words)
print(sentence)