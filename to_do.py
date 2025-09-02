from pathlib import Path

#  Defining the workspace and file path
workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
file_path = workspace / "to_do.txt"


task_list = []      # Created empty list

# Functions to perform operations
def add_task(user_task):        # For adding task to the list
    while True:
        try:
            if user_task == "":
                print("Task cannot be empty. Try again")
            elif user_task.isdigit():
                print("Task cannot be a number")
            else:
                task_list.append(user_task)
                return "Task added successfully!"
        except ValueError:
            print("\nTask cannot be a number!")
        except KeyboardInterrupt:
            print("\nProgram ended because of keyboard interrupt!")
        except Exception:
            print("\nUnexpected error occurred!")
            
            
def remove_task(user_task):     # For removing task from the list if it exists
        try:
            if user_task in task_list:
                task_list.remove(user_task)
                print("Task Successfully removed!")
            else:
                print(f"{user_task} cannot be found in the list!")
        except KeyboardInterrupt:
            print("\nProgram ended because of keyboard interrupt!")
        except Exception as e:
            print(f"\nUnexpected error occurred: {e}")
            

def save_tasks(file_path, user_task):
    while True:
        try:
            if file_path.exists():
                with open(file_path, "a", encoding="utf-8") as file:
                    for user_task in task_list:
                        file.write(user_task + "\n")
            else:
                print("File path doesn't exist, creating one...")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write("============List of Tasks Added============" + "\n")
                    file.write(user_task + "\n")
        except KeyboardInterrupt:
            print("\nProgram ended because of keyboard interrupt!")
        except Exception as e:
            print(f"\nUnexpected error occurred: {e}")
        return "Task saved successfully!"
    
    
def retrieve_tasks(file_path):     # For viewing tasks in the list
    try:
        if file_path.exists():
            print("========Your Task==========" + "\n")
            with open(file_path, "r", encoding="utf-8") as file:
                tasks = file.readlines()
                for task_no, task in enumerate(tasks):
                    print(f"{task_no +1}: {task}")
        else:
            print("No task found!")
    except KeyboardInterrupt:
        print("\nProgram ended because of keyboard interrupt!")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")
        

def tasks_completed(user_choice):
    status_completed = {"Tasks": user_choice, "Status": "Completed"}
    status_completed["Tasks"] = user_choice
    print(f"{user_choice} has been marked completed!")
    print(status_completed)



def main():
    while True:
        try:
            print("======== Welcome to PEN-DOWN TO-DO App ========\n")
            print("Kindly select the operation from the options below:")
            print("1. Add Task\n2. Remove Task\n3. Retrieve/View Tasks\n4. Mark Task as completed\n0. Exit the App")
            
            choice = int(input("\nSelect the preferred option from Above: "))
            
            if choice == 0:
                print("\nThanks for using PEN-DOWN TO-DO App. Do have a nice day!\n")
                break
            elif choice == 1:
                user_task = input("Enter the task you want to add: ")
                add_task(user_task)     # Calling the function to add user_task
                save_tasks(file_path, user_task)   # Calling the function to save user_task
            elif choice == 2:
                print("Below is the list of your tasks:")
                retrieve_tasks(file_path)
                user_task = input("Enter the task you want to remove: ")
                remove_task(user_task)
                save_tasks(file_path, user_task)
            elif choice == 3:
                retrieve_tasks(file_path)
            elif choice == 4:
                user_choice = input("Kindly enter the task already completed: ")
                tasks_completed(user_choice)
            else:
                print("Invalid options. Try again and follow the instructions!")
            
            # Ask the user for additional input (another operation)
            additional_task = input("Do you want to perform another operation? (Yes/No): ").strip().title()
            if additional_task != "Yes":
                print("\nThanks for using PEN-DOWN TO-DO App. Do have a nice day!\n")
                break
            
        except ValueError:
            print("\nOops! Kindly enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram ended because of keyboard interrupt!")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    
    
    # Run the Program 
if __name__ == "__main__":
    main()