def main():
    print("Welcome to To-Do List Manager")

if __name__ == "__main__":
    main()

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully")
