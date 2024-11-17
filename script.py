import argparse
import json
import os

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
    with open(task_file, 'w') as file:
        json.dump(tasks, file)

# Set up argument parser
parser = argparse.ArgumentParser(description='To-Do List Manager')

parser.add_argument("--tasklist", help="Custom tasks", default="Task-cli")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--add", help="The task to add")
group.add_argument("--list", action='store_true', help="List all tasks")
parser.add_argument("--update", help="Edit a task by providing new task description")
parser.add_argument("--delete",action='store_true',help ="Delete Tasks")
parser.add_argument("-i", "--index", type=int, help="The index of the task to update")
parser.add_argument("--format", choices=["json"], help="Output format")
args = parser.parse_args()

tasks = load_tasks()

# Add a new task
if args.add:
    tasks.append(args.add)
    save_tasks(tasks)
    print(f"{args.tasklist} added: {args.add}")

# List all tasks
if args.list:
    print("Current tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{args.tasklist} {idx}. {task}")

# Update a task
if args.update is not None and args.index is not None:
    if 0 <= args.index < len(tasks):
        old_task = tasks[args.index]
        tasks[args.index] = args.update
        save_tasks(tasks)
        print(f"Updated task {old_task} to {args.update}.")
    else:
        print("Invalid index. Please provide a valid task index.")

#Delete a task
if args.delete and args.index is not None:
    if 0 < args.index < len(tasks):
        removed_task = tasks.pop(args.index)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task}.")
    else:
        print("Invalid index. Please provide a valid task index.")
        

# Output in JSON format if specified
if args.format == "json" and args.list:
    print(json.dumps(tasks, indent=2))
