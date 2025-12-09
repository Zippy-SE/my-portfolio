print("--- Simple To-Do List Manager ---")
tasks = []

while True:
    print("\nOptions:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
    elif choice == '2':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f'Task "{task}" added.')
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
    elif choice == '4':
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 4.")