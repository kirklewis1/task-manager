import tkinter as tk
import operator

class Task:
    def __init__(self, name, status, deadline=None, priority=None):
        self.name = name
        self.status = status
        self.deadline = deadline
        self.priority = priority
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []
        
    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(f"Task '{task.name}' added.")
        
    def get_tasks(self):
        return self.tasks
    
    def update_task(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                self.history.append(f"Task '{task.name}' updated to status '{new_status}'.")
                return
        raise ValueError("Task not found.")
        
    def remove_task(self, task_name):
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                self.history.append(f"Task '{task.name}' removed.")
                del self.tasks[i]
                return
        raise ValueError("Task not found.")
    
    def sort_tasks(self, key, reverse):
        self.tasks.sort(key=operator.attrgetter(key), reverse=reverse)
        self.history.append(f"Tasks sorted by '{key}' in {'descending' if reverse else 'ascending'} order.")
        
    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        self.history.append(f"Tasks filtered by status '{status}'.")
        return filtered_tasks
    
    def search_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.history.append(f"Task '{name}' found.")
                return task
        raise ValueError("Task not found.")
    
    def get_completed_tasks(self):
        return len([task for task in self.tasks if task.status == "completed"])
    
    def get_task_history(self):
        return self.history
    
class TaskApp(tk.Tk):
    def __init__(self, task_manager):
        super().__init__()
        self.title("Task Manager")
        self.task_manager = task_manager
        
        self.name_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.deadline_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        
        self.name_label = tk.Label(text="Name:")
        self.name_entry = tk.Entry(textvariable=self.name_var)
        self.status_label = tk.Label(text="Status:")
        self.status_entry = tk.Entry(textvariable=self.status_var)
        self.deadline_label = tk.Label(text="Deadline:")
        self.deadline_entry = tk.Entry(textvariable=self.deadline_var)
        self.priority_label = tk.Label(text="Priority:")
        self.priority_entry = tk.Entry(textvariable=self.priority_var)
        
        self.add_button = tk.Button(text="Add", command=self.add_task)
        self.show_button = tk.Button(text="Show", command=self.show_tasks)
        self.update_button = tk.Button(text="Update", command=self.update_task)
        self.remove_button = tk.Button(text="Remove", command=self.remove_task)
        self.sort_button = tk.Button(text="Sort", command=self.sort_tasks)
        self.filter_button = tk.Button(text="Filter", command=self.filter_tasks)
        self.search_button = tk.Button(text="Search", command=self.search_task)
        self.history_button = tk.Button(text="History", command=self.show_history)
        
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.status_label.grid(row=1, column=0)
        self.status_entry.grid(row=1, column=1)
        self.deadline_label.grid(row=2, column=0)
        self.deadline_entry.grid(row=2, column=1)
        self.priority_label.grid(row=3, column=0)
        self.priority_entry.grid(row=3, column=1)
        
        self.add_button.grid(row=4, column=0)
        self.show_button.grid(row=4, column=1)
        self.update_button.grid(row=5, column=0)
        self.remove_button.grid(row=5, column=1)
        self.sort_button.grid(row=6, column=0)
        self.filter_button.grid(row=6, column=1)
        self.search_button.grid(row=7, column=0)
        self.history_button.grid(row=7, column=1)
        
    def add_task(self):
        name = self.name_var.get()
        status = self.status_var.get()
        deadline = self.deadline_var.get()
        priority = self.priority_var.get()
        
        self.task_manager.add_task(name, status, deadline, priority)
        
    def show_tasks(self):
        tasks = self.task_manager.get_tasks()
        message = "\n".join([str(task) for task in tasks])
        tk.messagebox.showinfo("Tasks", message)
        
    def update_task(self):
        name = self.name_var.get()
        status = self.status_var.get()
        deadline = self.deadline_var.get()
        priority = self.priority_var.get()
        
        self.task_manager.update_task(name, status, deadline, priority)
        
    def remove_task(self):
        name = self.name_var.get()
        self.task_manager.remove_task(name)
        
    def sort_tasks(self):
        self.task_manager.sort_tasks()
        
    def filter_tasks(self):
        status = self.status_var.get()
        tasks = self.task_manager.filter_tasks(status)
        message = "\n".join([str(task) for task in tasks])
        tk.messagebox.showinfo("Tasks", message)
        
    def search_task(self):
        name = self.name_var.get()
        task = self.task_manager.search_task(name)
        if task:
            message = str(task)
        else:
            message = "Task not found."
        tk.messagebox.showinfo("Task", message)
        
    def show_history(self):
        history = self.task_manager.get_task_history()
        message = "\n".join([str(entry) for entry in history])
        tk.messagebox.showinfo("History", message)

if __name__ == "__main__":
    task_manager = TaskManager()
    app = TaskApp(task_manager)
    app.mainloop()

        


