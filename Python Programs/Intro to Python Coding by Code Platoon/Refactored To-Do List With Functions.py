def show_menu():
    print("Options: ")
    print("1. View Tasks")
    print("2. Add A Task")
    print("3. Remove A Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i in range(len(tasks)):
            print(f"{i +1}. {tasks[i]}")

def add_task(tasks):
    new_task = input("Enter the task you want to add: ")
    tasks.append(new_task)
    print(f'Task "{new_task}" added.')

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
    else:
        view_tasks(tasks)
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")

#list_of_tasks = ["Clean our room"]
#show_menu()
#view_tasks(list_of_tasks)
#add_task(list_of_tasks)
#remove_task(list_of_tasks)
#view_tasks(list_of_tasks)

tasks = []
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
