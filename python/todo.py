import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a", encoding= "utf-8") as file:
      file.write(task + "\n")
     
     

def list_tasks(): 
   if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r", encoding= "utf-8") as file: 
        tasks = file.readlines()
        output_string = ""
        counter = 1
        for tasks in tasks:
            output_string = output_string
   return output_string


def remove_task(index):

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, counter=1):
                if i != index:
                    file.write(task)
        print("Task Removed :)")
    else:
        print("No Tasks Found :(")


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
                        "-a",
                        "--add",
                        help = "Add a new task todo"
                        )
    parser.add_argument(
                        "-l",
                        "--list",
                        action="store_true",
                        help = "List all todo tasks")
    parser.add_argument(
                        "-r",
                        "--remove",
                        help = "Remove a task todo by index")

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
        
 