tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        print("Exiting To-Do App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
