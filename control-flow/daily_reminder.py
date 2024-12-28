task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        chosen_task = "is a low priority task"
    case "medium":
        chosen_task = "is a medium priority task"
    case "low":
        chosen_task = "is a low priority"
    case _:
        print("Not a valid priority option")

        if time == "yes":
            print("Reminder:",task,chosen_task,"that requires immediate attention today!" )
        else:
            print("Note:",task,chosen_task,".Consider completing it when you have free time.")
