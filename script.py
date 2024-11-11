import argparse
import json
import os

task_file = "tasks.json"
def load_tasks():
    if os.path.exists(task_file):
        try:
            with open(task_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("No existing task file found. A new one will be created.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON from the task file. The file may be corrupted.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []
    else:
        print("No existing task file found. A new one will be created.")
        return []
    
def save_tasks(tasks):
    with open(task_file, 'w')as file:
        json.dump(tasks,file)
        
parser = argparse.ArgumentParser(description='To-Do List Manager')

parser.add_argument("--tasklist", help="Custom tasks", default="Task-cli")
group = parser.add_mutually_exclusive_group()
group.add_argument("--add",help ="the task to add")
group.add_argument("--list",help ="List all tasks")
parser.add_argument('update', nargs='?', help='Edit a task by ID')
parser.add_argument("--format", choices = ["json"], help = "Output format")
args = parser.parse_args()

tasks = load_tasks()


if args.add:
    tasks.append(args.add)
    save_tasks(tasks)
    print(f"{args.tasklist} add : {args.add}")

if args.list:
    print ("Current tasks:")
    for idx, task in enumerate(tasks, start =1):
        print(f"{args.tasklist} {idx}. {task}")
        
if args.format == "json" and args.list:
    print(json.dumps(tasks, indent=2))


