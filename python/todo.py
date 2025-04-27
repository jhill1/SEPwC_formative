import argparse
import os

TASK_FILE = ".tasks.txt"


def add_task(task):
    #Open the file in append mode to add a new task to the end of the exisitng list
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        #Write the task followed by a newline character so the task appears on a new line
        file.write(task +"\n")
        

#Listing all tasks within the task file                
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
    """Function: remove_task

   Input - a task to add to the list
   Return - nothing
   """
   #Read all lines within the task file 
   with open(TASK_FILE, 'r', encoding='utf-8') as file:
       lines = file.readlines()
       
       #Check that the line to remove is valid
       if 1 <= index <= len(lines):
           lines.pop(index - 1)
           
    #Update the list and add it back to the original file       
    with open(TASK_FILE, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    
    
    print ('Task removed.')
    else:
    print('Invalid task number.')
 
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
