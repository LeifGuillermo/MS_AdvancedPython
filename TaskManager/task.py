from collections import deque
from decorators import log_action, timer

class TaskManager:
    """
    A class to manage tasks using a queue.
    """

    def __init__(self, filename="queue.txt"):
        """
        Initializes the TaskManager with a filename and loads tasks from the file.

        Args:
            filename (str): The name of the file to store tasks. Defaults to "queue.txt".
        """
        self.tasks = deque()  # Use deque to store tasks
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the specified file."""
        with open(self.filename) as file:
            line = file.readline()
            if line.strip():
                task_name, due_date, completed, description, assignedTo, impact, effort = line.strip().split(',')
                new_task = {
                    "name": task_name,
                    "due_date": due_date,
                    "completed": completed == "True",
                    "description": description,
                    "assignedTo": assignedTo,
                    "impact": impact,
                    "effort": effort
                }
                self.tasks.append(new_task)  # Add task to queue

    @log_action
    def add_task(self, name, due_date, description, assignedTo, impact, effort):
        """
        Adds a new task to the task queue.

        Args:
            name (str): The name of the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
            description (str): A description of the task.
        """
        new_task = {
            "name": name,
            "due_date": due_date,
            "completed": False,
            "description": description,
            "assignedTo": assignedTo,
            "impact": impact,
            "effort": effort
        }
        self.tasks.append(new_task)
        self.save_tasks_to_file()

    @log_action
    def update_task(self, index, name, due_date, description, assignedTo, impact, effort):
        """
        Adds a new task to the task queue.

        Args:
            name (str): The name of the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
            description (str): A description of the task.
        """
        new_task = {
            "name": name,
            "due_date": due_date,
            "completed": False,
            "description": description,
            "assignedTo": assignedTo,
            "impact": impact,
            "effort": effort
        }
        self.tasks.insert(index-1, new_task)
        self.tasks.append(new_task)
        self.save_tasks_to_file()

    @log_action
    def view_tasks(self):
        """Display all tasks in the task queue."""
        if not self.tasks:
            print("No tasks in the queue.")
            return
        # Print tasks in the order they were added
        for index in range(len(self.tasks)):
            print(index+1, self.task_to_string(self.tasks[index]))
        
    @log_action
    def mark_complete(self, task_index):
        """Mark a task as complete."""
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            del self.tasks[task_index]
            task["completed"] = True
            self.save_completed_task(task)  # Save the completed task to a file
            self.save_tasks_to_file()
            print(f"Task '{task['name']}' marked as complete.")
        else:
            print("Task not found.")

    @log_action
    def edit_task(self, index):
        """Edit a task's field values"""
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            del self.tasks[index]
            name = input(f"Update name from {task['name']} to:")
            due_date = input(f"Update due date from {task['due_date']} to:")
            description = input(f"Update description from {task['description']} to:")
            assignedTo = input(f"Update assigned to from {task['assignedTo']} to:")
            impact = input(f"Update impact from {task['impact']} to:")
            effort = input(f"Update effort from {task['effort']} to:")
            self.update_task(index, name, due_date, description, assignedTo, impact, effort)
        else:
            print("Task not found.")

    @timer
    def save_tasks_to_file(self):
        """Save the tasks to the specified file."""
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['name']},{task['due_date']},{task['completed']},{task['description']},{task['assignedTo']},{task['impact']},{task['effort']}\n")

    @log_action
    @timer
    def save_completed_task(self, task):
        """Save the completed task to a separate file."""
        with open("completed_tasks.txt", 'w') as f:
            f.write(f"{task['name']},{task['due_date']},{task['completed']},{task['description']},{task['assignedTo']},{task['impact']},{task['effort']}\n")

    def task_to_string(self, task):
        """Convert a task dictionary to a string representation."""
        completed_mark = "x" if task["completed"] else " "
        return f"[{completed_mark}] {task['name']} (Due: {task['due_date']}) - {task['description']} - assigned-to:{task['assignedTo']} - impact:{task['impact']} - effort:{task['effort']} "

    @log_action
    def view_next_queue_task(self):
        """View the next task in the task queue without removing it."""
        if not self.tasks:
            return "No tasks in the queue."
        next_task = self.tasks[0]  # Peek at the next task
        return self.task_to_string(next_task)