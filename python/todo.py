
import argparse
import os

#all functions read from here
TASK_FILE = "todo.txt"

#allows users to add text to a file called todo.txt
def add_task(task_name):
    """Function: add_task"""
    with open (TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task_name + "\n")
    print (f"Task '{task_name}' added successfully!")


#allows users to remove a task from the todo.txt file
def remove_task(task_index):
    """Function: remove_task"""
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return
    
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()

    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
        return
    
    del tasks[task_index - 1]

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        file.writelines(tasks)
    print("Task removed successfully!")


#lists all tasks in the todo.txt file
def list_tasks():
    """Function: list_tasks"""
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return
    
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]
    
    if not tasks:
        print("No tasks found.")
        return ""
    
    return "\n".join(f"{i + 1}. {task}" for i, task in enumerate (tasks))




def main():
    #sets command-line arguments
    parser = argparse.ArgumentParser(description="To-Do List Application")
    parser.add_argument("-a", "--add", help="Add a new task to the to-do list")
    parser.add_argument("-r", "--remove", help="Remove a task from the to-do list")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks in the to-do list")

    args = parser.parse_args()

   #logic to determine which action to take based on the user's input
    if args.add:
        add_task(args.add)
    elif args.remove:
        remove_task(args.remove)
    elif args.list:
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()