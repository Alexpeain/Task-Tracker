import argparse
import json
import os
from datetime import datetime

task_file = "tasks.json"

def load_tasks():
    if os.path.exists(task_file):
        try:
            with open(task_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")
            return []
    else:
        print("No existing task file found. A new one will be created.")
        return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        file.write(json.dumps(tasks))  
        
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='To-Do List Manager')

    parser.add_argument("--tasklist", help="Custom tasks", default="Task-cli")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--add", help="The task to add")
    group.add_argument("--list", action='store_true', help="List all tasks")
    parser.add_argument("--list-done",action="store_true",help="List done task")
    parser.add_argument("--list-in-progress",action="store_true",help="List in progres task")
    parser.add_argument("--list-todo",action="store_true",help="List todo tasks")
    parser.add_argument("--update", help="Edit a task by providing new task description")
    parser.add_argument("--delete",action='store_true',help ="Delete Tasks")
    parser.add_argument("--delete-all", action='store_true', help="Delete all tasks")
    parser.add_argument("--mark-done", action='store_true',help="Mark as Done")
    parser.add_argument("--mark-todo",action='store_true',help ="Mark Todo")
    parser.add_argument("--mark-in-progress",action='store_true',help="Mark In Progress")
    parser.add_argument("-i", "--index", type=int, help="The index of the task to update")
    parser.add_argument("--format", choices=["json"], help="Output format")
    args = parser.parse_args()

    tasks = load_tasks()

    # Add a new task
    if args.add:
        now = datetime.now().isoformat()
        task_index = len(tasks)
        tasks.append({
            "id": args.index,
            "description": args.add,
            "status": "TODO",
            "createdAt": now,
            "updatedAt": now })
        save_tasks(tasks)
        print(f"{args.tasklist} Task added successfully (ID: {task_index})")

    # List all tasks
    if args.list:
        print("Current tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{args.tasklist} {idx}. {task['description']} [{task['status']}] "
                f"(Created at: {task['createdAt']}, Updated at: {task['updatedAt']})")

    #ListDone
    if args.list_done:
        print("Complete tasks:")
        completed_tasks = [task for task in tasks if task['status'] == 'Done']
        if completed_tasks:
            for idx,task in enumerate(completed_tasks, start=1):
                print(f"{args.tasklist} {idx}. {task['description']} - Status: {task['status']}")
        else:
            print("No completed tasks found.")
            
    #list-in-Progress 
    if args.list_in_progress:
        print("List in Progress: ")
        in_progress_tasks = [task for task in tasks if task['status'] == 'IN_PROGRESS']
        if in_progress_tasks:
            for idx,task in enumerate(in_progress_tasks,start=1):
                print(f"{args.tasklist} {idx}. {task['description']} - Status: {task['status']}")
        else:
            print("No in progress tasks found.")

    #list-todo
    if args.list_todo:
        print("List Todo")
        todo_tasks = [task for task in tasks if task['status'] == 'TODO']
        if todo_tasks:
            for idx,task in enumerate(todo_tasks,start=1):
                print(f"{args.tasklist} {idx}. {task['description']} - Status: {task['status']}")
        else:
            print("No To Do tasks found.")
                
    # Update a task
    if args.update is not None and args.index is not None:
        if 0 <= args.index < len(tasks):
            old_task = tasks[args.index]
            tasks[args.index]['description'] = args.update
            tasks[args.index]['updatedAt'] =datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {args.index} updated successfully.")
        else:
            (f"Task with ID {args.index} not found.")

    #Delete a task
    if args.delete and args.index is not None:
        if 0 < args.index < len(tasks):
            removed_task = tasks.pop(args.index)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task['description']}.")
        else:
            print("Invalid index. Please provide a valid task index.")
    #Delete all tasks
    if args.delete_all:
        tasks.clear()
        save_tasks(tasks)
        print("All tasks have been deleted.")

    #Mark Done,todo, in-progress
    if args.mark_done and  args.index is not None:
        if 0 < args.index < len(tasks):
            tasks[args.index]['status'] = 'Done'
            save_tasks(tasks)
            print(f"Task marked as done: {tasks[args.index]['description']}.")
        else:
            print("Invalid index.")

    if args.mark_in_progress and args.index is not None:
        if 0 <= args.index < len(tasks):
            tasks[args.index]['status'] = 'IN_PROGRESS'
            save_tasks(tasks)
            print(f"Task marked as in progress: {tasks[args.index]['description']}.")
        else:
            print("Invalid index.")

    if args.mark_todo and args.index is not None:
        if 0 <= args.index < len(tasks):
            tasks[args.index]['status'] == 'TODO'
            save_tasks(tasks)
            print(f"Task marked as To Do: {tasks[args.index]['description']}.")
        else:
            print("Invalid index.")
                
    # Output in JSON format if specified
    if args.format == "json" and args.list:
        print(json.dumps(tasks, indent=2))

