"""
todo.py is a simple to-do list application that
keeps a users to-do list as a text file.

Users can add, list or remove tasks
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
    """Function: list_tasks

    Input - a task to add to the list
    Return - a string of the tasks on the list
    """

    output_string = ""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                output_string += (f"{index}. {task.strip()}\n")
    return output_string.strip()



def remove_task(index):
    """Function: remove_task

    Input - a task to add to the list
    Return - nothing
    """

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed.")
    else:
        print("No tasks found.")


def main():