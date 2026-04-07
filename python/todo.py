"""Todo.py is a simple GUI based to do list where you can add tasks
and remove tasks and list them"""

import argparse

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
Input - a task to add to the list
Return - nothing"""

    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")

def list_tasks():
    """Function: list_tasks
Imput -l
output shows a list of the items in list"""

    with open (TASK_FILE,"r", encoding="utf-8") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""
        for task in tasks:
            output_string = output_string + str(counter)+". "+task
            counter=counter+1

    return output_string.rstrip('\n')


def remove_task(index):
    """function: remove_task,
Imput -r index to remove a task
Return Removed.."""

    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines() #TASK_FILE is read :)

        if 0 < index <= len(lines):
            removed = lines.pop(index - 1) #removes lines according to index

            with open(TASK_FILE, "w", encoding="utf-8") as file: #w overwrites
                file.writelines(lines)

            print(f"Removed: {removed.strip()}")
        else:
            print("sorry, there is no task to remove")

    except FileNotFoundError:
        print("Error, no tasks found. Create one!!")

def main():
    """parser allowing command line arguments,
imput -a (add),-l (list),-r (remove)
output allows user to interact witht the code"""
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
