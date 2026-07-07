# match-case provides a cleaner way to handle multiple possible values.
# Available in Python 3.10 and later.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")

# Matching strings
command = "start"

match command:
    case "start":
        print("Starting application...")
    case "stop":
        print("Stopping application...")
    case "restart":
        print("Restarting application...")
    case _:
        print("Unknown command")