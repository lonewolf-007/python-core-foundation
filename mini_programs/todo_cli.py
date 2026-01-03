tasks = []

def show_tasks():
    """Display all added tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    user_choice = input("Choose an option (1/2/3): ")

    if user_choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task added successfully.")

    elif user_choice == "2":
        show_tasks()

    elif user_choice == "3":
        print("Exiting To-Do App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
