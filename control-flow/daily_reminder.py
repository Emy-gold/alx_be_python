# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for valid priority level
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
        break
    else:
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Prompt for time-bound flag
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Process the task using match case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Modify the message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", message)

# Optional completion message
print("\n✅ Well done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
