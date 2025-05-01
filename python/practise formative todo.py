# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:17:13 2025

@author: evepl
"""
import argparse
import os # os is not strictly needed here if using try/except for file handling

TASK_FILE = ".tasks.txt"

def add_task(task):
    """
    Function: add_task
    Adds a task to the task file.

    Input: task (string) - The task description to add.
    Return: None
    """
    try:
        # Open file in append mode ('a'), creates file if it doesn't exist
        # Use utf-8 encoding for wider character support
        with open(TASK_FILE, "a", encoding="utf-8") as file:
            file.write(task + "\n") # Add newline for separation
        print(f"Task added: \"{task}\"")
    except IOError as e:
        print(f"Error writing to task file {TASK_FILE}: {e}")


def list_tasks():
    """
    Function: list_tasks
    Reads tasks from the file and returns a formatted, numbered list.

    Input: None
    Return: string - Formatted list of tasks or a message if no tasks exist.
    """
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()

        if not tasks:
            return "No tasks found."

        output_string = "Tasks:\n"
        counter = 1
        for task in tasks:
            # Strip newline characters for clean output
            output_string += f"{counter}. {task.strip()}\n"
            counter += 1
        # Remove the last newline character for cleaner printing
        return output_string.strip()

    except FileNotFoundError:
        return "No tasks found (task file does not exist)."
    except IOError as e:
        return f"Error reading task file {TASK_FILE}: {e}"


def remove_task(index):
    """
    Function: remove_task
    Removes a task from the file by its 1-based index.

    Input: index (int) - The 1-based index of the task to remove.
    Return: None
    """
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to remove.")
            return

        # Validate index (convert 1-based index to 0-based)
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1).strip() # Remove task and get its value

            # Write the remaining tasks back to the file (overwrite mode 'w')
            with open(TASK_FILE, "w", encoding="utf-8") as file:
                file.writelines(tasks)
            print(f"Removed task {index}: \"{removed_task}\"")
        else:
            print(f"Error: Invalid task index '{index}'. Use --list to see valid indices.")

    except FileNotFoundError:
        print("No tasks to remove (task file does not exist).")
    except IOError as e:
        print(f"Error accessing task file {TASK_FILE}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
        "-a",
        "--add",
        metavar='TASK', # Helps usage message
        help="Add a new task (e.g., --add \"Buy groceries\")"
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List all tasks"
    )
    parser.add_argument(
        "-r",
        "--remove",
        metavar='INDEX', # Helps usage message
        help="Remove a task by its index (e.g., --remove 2)"
    )

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks_output = list_tasks()
        print(tasks_output) # Print the returned string
    elif args.remove:
        try:
            task_index = int(args.remove)
            if task_index <= 0:
                 print("Error: Task index must be a positive number.")
            else:
                 remove_task(task_index)
        except ValueError:
            print(f"Error: Invalid index '{args.remove}'. Please provide a number.")
    else:
        # Show help if no arguments are provided
        parser.print_help()


if __name__ == "__main__":
    main()
