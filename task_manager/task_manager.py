# task_manager.py

import json
import os



class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False  # Default to not completed

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


tasks = []  # List to hold tasks
task_id_counter = 1  # To assign unique IDs to tasks

def add_task(title):
    global task_id_counter
    task = Task(task_id_counter, title)
    tasks.append(task)
    task_id_counter += 1
    print(f"Added task: {task}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "✔️" if task.completed else "❌"
            print(f"[{status}] {task.id}: {task.title}")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Deleted task with ID: {task_id}")

def mark_task_as_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Marked task {task_id} as complete.")
            return
    print(f"Task with ID {task_id} not found.")


def save_tasks(filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)
    print("Tasks saved.")

def load_tasks(filename='tasks.json'):
    global tasks, task_id_counter
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            task_data = json.load(file)
            tasks = [Task(**data) for data in task_data]
            task_id_counter = max(task.id for task in tasks) + 1 if tasks else 1
        print("Tasks loaded.")
    else:
        print("No saved tasks found. Starting with an empty task list.")


def main():
    load_tasks()  # Load tasks at the start
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_as_complete(task_id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()  # Save before exiting
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()