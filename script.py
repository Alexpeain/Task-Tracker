import argparse

parser = argparse.ArgumentParser(description='To-Do List Manager')

parser.add_argument("--tasklist", help="Custom tasks", default="Task-cli")
parser.add_argument("add",help ="the task to add")
parser.add_argument("--format", choices = ["json","xml"], help = "Output format")

args = parser.parse_args()

#print(f"{args.greet}, {args.name}{args.age}!")
#print(f"Task List: {args.tasklist}, Adding Task: {args.add}")
print(f"{args.tasklist} add : {args.add}")
