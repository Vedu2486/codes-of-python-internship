# Simple To-Do List Program

# Initialize an empty list to store tasks
to_do_list = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task you want to add: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    view_tasks()
    if to_do_list:
        try:
            task_number = int(input("Enter the task number you want to remove: "))
            if 1 <= task_number <= len(to_do_list):
                removed_task = to_do_list.pop(task_number - 1)
                print(f"'{removed_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
