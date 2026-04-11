"""
this module handles the logic for a To-Do list application.
"""

import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")

def list_tasks():
    """Function: list_task
    
    Input - a task to add to the list
    Return - a stirng to the list
    """
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
    numbered_tasks = []
    for i, task in enumerate(tasks, start=1):
        formatted_line = f"{i}. {task.strip()}"
        numbered_tasks.append(formatted_line)
    return "\n".join(numbered_tasks)

def remove_task(index):
    """Function: remove_task
    
    Input - a task to remove the list
    Return - nothing 
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        if index < 1 or index > len(tasks):
            return
        tasks.pop(index - 1)
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            file.writelines(tasks)

def main():
    """Function:main
    
    Input - nothing
    Return - nothing
    """
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
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
