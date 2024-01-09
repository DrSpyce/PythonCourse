import os


def load_tasks(file_name):
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                index, task = line.split(" ", 1)
                tasks[int(index)] = task
    return tasks


def save_tasks(tasks, file_name):
    with open(file_name, "w") as file:
        for index, task in tasks.items():
            file.write(f"{index} {task}\n")


def add_task(task, tasks):
    index = max(tasks.keys(), default=0) + 1
    tasks[index] = task
    print(f"Task '{task}' added with index {index}.")


def mark_done(task_index, tasks):
    if task_index in tasks:
        tasks[task_index] = f"[Done] {tasks[task_index]}"
        print(f"Task '{tasks[task_index]}' marked as done.")
    else:
        print("Invalid task index.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in tasks.items():
            print(f"{index}. {task}", end="")


file_name = "tasks.txt"
tasks = load_tasks(file_name)

while True:
    print("\nCommand Menu:")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. List Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task, tasks)
    elif choice == "2":
        list_tasks(tasks)
        task_index = int(input("Enter the task index to mark as done: "))
        mark_done(task_index, tasks)
    elif choice == "3":
        list_tasks(tasks)
    elif choice == "4":
        save_tasks(tasks, file_name)
        print("Exiting. Tasks saved.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

