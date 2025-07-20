# daily_reminder.py

# Ask for the task
task = input("Enter your task: ")

# Ask for the priority level
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter a valid priority: high, medium, or low.")

# Ask if time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
        break
    print("Please enter yes or no.")

# Match Case and direct Reminder print
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
