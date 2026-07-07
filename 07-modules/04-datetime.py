# The datetime module is used to work with dates and times.

from datetime import datetime

# Current date and time
current_time = datetime.now()

print(f"Current date and time: {current_time}")

# Individual components
print(f"Year: {current_time.year}")
print(f"Month: {current_time.month}")
print(f"Day: {current_time.day}")

# Format a date
formatted_date = current_time.strftime("%d-%m-%Y")
formatted_time = current_time.strftime("%I:%M:%S %p")

print(f"Formatted date: {formatted_date}")
print(f"Formatted time: {formatted_time}")

# Create a specific date
birthday = datetime(2005, 5, 15)

print(f"Birthday: {birthday.strftime('%d %B %Y')}")