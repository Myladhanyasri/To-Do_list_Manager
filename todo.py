def delete_task(tasks,index):
    tasks.pop(index)
def main():
    print("Welcome to To-Do List Manager")

if __name__ == "__main__":
    main()

def delete_task(tasks, index): if 0 <= index < len(tasks): 
        tasks.pop(index) print("Task deleted successfully")
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully")
    else:
        print("Invalid task number")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i+1}. {task['task']} [{status}]")

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully")

