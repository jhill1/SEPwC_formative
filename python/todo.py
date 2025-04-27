import argparse
import os

TASK_FILE = ".tasks.txt"

#Adding a new task to the end of the to-do list
def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
      file.write(task + "\n")

                 
def list_tasks():
    
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""
        for task in tasks:
            output_string = output_string + str(counter) + ". " +task
            counter = counter + 1
            #Code from Gemini
            my_string = '1. Item 1\n2. Item 2\n3. Item 3\n4. Item 4\n5. Item 5\n'
            modified_string = my_string[:-1]
            print(modified_string)
            
    return modified_string


def remove_task(index):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        tasks = file.readlines()

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
