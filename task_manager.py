"""
Created on Wed Dec 16 19:42:43 2025

@author: anastasiiavereshchak
"""
import numpy as np
import database


def add_task(tasks):
    name = input("Task name: ")
    priority = int(input("Priority (1=High, 3=Low): "))
    task = (name, priority, False)

    tasks.append(task)
    database.save_tasks(tasks)

    print("Task added!")


def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, (name, priority, completed) in enumerate(tasks, 1):
        status = "Done" if completed else "Pending"
        print(f'{i}. {name} , Priority: {priority} , {status}')


def complete_task(tasks):
    show_tasks(tasks)
    idx = int(input("Select task number to mark as completed: ")) - 1
    name, priority, _ = tasks[idx]
    tasks[idx] = (name, priority, True)
    database.save_tasks(tasks)
    print("Task marked as completed!")


def task_statistics(tasks):
    done = np.array([t[2] for t in tasks], dtype=bool)  # <-- ARRAY usage
    stats = {
        "total": len(tasks),
        "completed": int(done.sum()),
        "pending": int((~done).sum())
    }

    print("Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")


def main():
    tasks = database.load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Show statistics")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            task_statistics(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()