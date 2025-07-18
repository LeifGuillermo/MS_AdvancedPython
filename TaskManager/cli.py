# THIS FILE SHOULD NOT BE MODIFIED
from task import TaskManager

def display_menu():
    """Display the menu options for the Task Manager."""
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Mark Task Complete")
    print("5. View Next Task")
    print("6. Exit")

def main():
    """Main function to run the Task Manager CLI."""
    task_manager = TaskManager()  # Initialize TaskManager

    while True:
        display_menu()  # Show the menu
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            
            name = input("Enter the task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            description = input("Enter a description for the task: ")
            assignedTo = input("Enter user name to assign to: ")
            priority = input("Enter a priority (1-5): ")
            effort = input("Enter effort required for this task (1-5): ")
            
            # Add the task using the TaskManager
            task_manager.add_task(name, due_date, description, assignedTo, priority, effort)
            print(f"Task '{name}' added.")

        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            if not task_manager.tasks:  # Check if there are no tasks
                print("No tasks available to edit.")
            else:
                task_manager.view_tasks()  # Show tasks to select from
                task_number = input("Enter task number to edit: ")
                if task_number.isdigit():
                    task_index = int(task_number) - 1  # Convert to zero-based index
                    task_manager.edit_task(task_index)
                else:
                    print("Invalid task number.")
        elif choice == "4":
            if not task_manager.tasks:  # Check if there are no tasks
                print("No tasks available to mark as complete.")
            else:
                task_manager.view_tasks()  # Show tasks to select from
                task_number = input("Enter task number to mark as complete: ")
                if task_number.isdigit():
                    task_index = int(task_number) - 1  # Convert to zero-based index
                    task_manager.mark_complete(task_index)
                else:
                    print("Invalid task number.")

        elif choice == "5":
            next_task = task_manager.view_next_queue_task()  # Get the next task
            print(next_task)  # Display the next task

        elif choice == "6":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()