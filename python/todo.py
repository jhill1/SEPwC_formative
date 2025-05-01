import argparse
import os


TASK_FILE = ".tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")
    return
        
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """

def list_tasks():
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""
        for task in tasks:
            output_string = output_string + str(counter) + ". "+task
            counter = counter + 1
        output_string = output_string.rstrip('\n')
    
    return output_string


def remove_task(index):
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        if index == 0 or index > len(tasks):
            return 
        del tasks[index - 1]
        
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task.strip()}\n") 


    return

def main():
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
