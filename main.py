"""
An Expense Tracker is a practical application that
allows users to log their daily expenses and track spending
habits. This project enhances knowledge of file handling,
data storage, and user input processing in Python.
This chapter covers the step-by-step implementation of an
Expense Tracker, including user input handling, data storage
in a CSV file, and displaying expense reports.

Key Concepts of Expense Tracker in Python

Data Handling:

Using lists and dictionaries to store
expenses
Writing and reading data from a CSV file

User Input Processing:

Taking user input for expense details
Validating and formatting input data

Report Generation:

Displaying total expenses per category
Summarizing daily or monthly spending

"""







"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

#  To do list
from pathlib import Path
workspace = Path("To do")
workspace.mkdir(exist_ok= True)
text_file = workspace / "list.txt"


task_to_do = []

def tasks_added(user_task):
    task_to_do.append(user_task)
    # with open(text_file, "w", encoding= "utf-8") as f:
    #     writer = f.readlines()
    #     tasks_added(f, writer, user_task)
        
    print(f"{user_task} added successfully!\n")

def tasks_remove(user_task):
    if user_task in task_to_do:
        task_to_do.remove(user_task)
        print(f"{user_task} successfully removed!\n")
    else:
        print(f"Task {user_task} not found!")

def tasks_retrieve():
    if task_to_do:
        print("=" *20)
        for tasks_number, tasks in enumerate(task_to_do):
            print(f"{tasks_number + 1}: {tasks}")
    else:
        print("No Task found!")

def tasks_completed(user_choice):
    status_completed = {"Tasks": user_choice, "Status": "Completed"}
    status_completed["Tasks"] = user_choice
    print(f"{user_choice} has been marked completed!")
    print(status_completed)

while True:
    try:
        #  Options to select from
        print("1. Add task  2. Remove task  3. Retrieve task  4. Mark task as completed 0. Exit")
        choice = input("Kindly enter your choice: ")
        if choice == "1":
            user_task = input("Kindly enter the task to be added: ")
            tasks_added(user_task)
        elif choice == "2":
            user_task = input("Kindly enter the task to be removed: ")
            tasks_remove(user_task)
        elif choice == "3":
            print("\nThe list of your tasks is as follow: ")
            tasks_retrieve()
        elif choice == "4":
            user_choice = input("Kindly enter the task already completed: ")
            tasks_completed(user_choice)
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Try again!")
    except TypeError:
        print("A positional Argument occurred!")

    except KeyboardInterrupt:
        print("The program ended due to keyboard interrupt!")


