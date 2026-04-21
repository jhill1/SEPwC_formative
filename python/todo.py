"""scipt to write and edit a list of tasks"""
import os
import argparse
import sys

TASK_FILE = ".tasks.txt" if os.path.exists(".tasks.txt") else "list.txt"

def add_task(task):
    """Function: add_task

    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")
    #print(f"{task} has been added to your list")

def list_tasks():
    """Function: List_task
    
    Input - nothing 
    Return - a list of the tasks
    """
    #check if the file exists first
    if not os.path.exists(TASK_FILE) or os.path.getsize(TASK_FILE) == 0:
        return ""

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines() if line.strip()]

    return "\n".join([f"{i}. {task.strip()}" for i, task in enumerate(tasks,1)])

def remove_task(index):
    """Functions: remove_task
    
    Input - a task to be removed from the list
    Return - nothing
    """
    #read the current list of tasks
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        #check the specific task
    if 0< index <= len(tasks):
        tasks.pop(index - 1)
        #remove the task
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            file.writelines(tasks)
        print(f"Task {index} removed successfully.")
    else:
        print(f"Error: Task {index} does not exist.")

def main():
    """main function to handle arguments."""
    # Force Windows to stop adding \r characters automatically
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(newline='\n')
        except AttributeError:
            # Fallback for older Python versions
            pass
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        if tasks:
            print(tasks.replace("\r", ""), end="\n")
        else:
            print("", end="")
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
