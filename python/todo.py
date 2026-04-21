"""Simple command line todo list application"""

import argparse

TASK_FILE = ".tasks.txt"


def add_task(task):
    """Function: add_task

    Adds a task to out save file

    Input - a task to add to the list
    Return - nothing
    """

    with open(TASK_FILE, "a", encoding="utf-8") as f:
        f.write(task + "\n")

def list_tasks():
    """Function: list_tasks

    Lists all of the tasks saved to the file

    Input - nothing
    Return - result

    """

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = ""
    for i, line in enumerate(lines, start=1):
        if i == len(lines):
            result += f"{i}. {line.strip()}"
        else:
            result += f"{i}. {line.strip()}\n"
    return result


def remove_task(index):
    """Function: remove a task by its index

    Input - a task to remove
    Return - nothing

    """

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if index < 1 or index > len(lines):
        return
    lines.pop(index-1)

    with open(TASK_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return

def main():
    """Handle command-line arguments and run the todo app."""
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
