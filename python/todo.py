
#3 commands for user: list add and remove

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


#begins with options for the user to choose from
print("Welcome to your To-Do List Manager!")
options = '''
Please choose an option:
1. Add a task
2. Remove a task
3. List all tasks
4. Exit
'''

while True:
    print(options)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        new_task = input("What do you need to do? ")
        add_task(new_task)

    elif choice == "2":
        task_to_remove = input("Which task do you want to remove? ")
        remove_task(task_to_remove)

    elif choice == "3":
        list_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")