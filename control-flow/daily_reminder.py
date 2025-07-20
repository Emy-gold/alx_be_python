# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Optional loop to confirm valid priority
while priority not in ("high", "medium", "low"):
    print("Please enter a valid priority: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Provide reminder based on priority and time-bound flag
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Check if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Output the final reminder
print("\nReminder:", message)
