def main():
    print("Welcome to To-Do List Manager")

if __name__ == "__main__":
    main()
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully")
