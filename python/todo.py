
import argparse
import os

#allows users to add text to a file called todo.txt
def add_task(task_name):
    with open ("todo.txt", "a") as file:
        file.write(task_name + "\n")
    print (f"Task '{task_name}' added successfully!")


#allows users to remove a task from the todo.txt file
def remove_task(task_name):
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    with open("todo.txt", "w") as file:
        for task in tasks:
            if task.strip() != task_name:
                file.write(task)

    print(f"Task '{task_name}' removed successfully!")


#lists all tasks in the todo.txt file
def list_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if tasks:
        print("Your To-Do List:")
        for task in tasks:
            print("- " + task.strip())
    else:
        print("Your To-Do List is empty.")



def main():
    #sets command-line arguments
    parser = argparse.ArgumentParser(description="Simple To-Do List Application")

#
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