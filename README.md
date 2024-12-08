# Task Tracker CLI

A simple command line interface (CLI) application to track and manage your tasks. This application allows users to add, update, delete, and list tasks, all stored in a JSON file.

## Features

- **Add Tasks**: Add new tasks to your task list.
- **Update Tasks**: Modify existing tasks with new descriptions.
- **Delete Tasks**: Remove tasks from your list.
- **Mark Tasks**: Mark tasks as "in progress" or "done".
- **List Tasks**: View all tasks or filter by status (done, in progress, or todo).

## Requirements

- The application should run from the command line.
- Accept user actions and inputs as arguments.
- Store tasks in a JSON file located in the current directory.
- If the JSON file does not exist, it should be created automatically.
- Use the native file system module of your programming language to interact with the JSON file.
- No external libraries or frameworks should be used.
- Handle errors and edge cases gracefully.

## Commands

Here are the commands available in the Task Tracker CLI:
## Add Tasks

```bash
   python script.py --add "Add the tasks"
```

## Update Tasks

```bash
    python script.py --update "Update the Tasks" -1 10
```

## Delete Tasks

```bash
    python script.py --delete -i 0 # i is for index flag and 0 is index to delete
```

## Delete All

```bash
    python script.py --delete-all #reset all
```

## List all

```bash
    python script.py --list
```

## List Done

```bash
    python script.py --list-done  #list Done Tasks
```

## List In Progress

```bash
    python script.py --list-in-progress  #list  Tasks in Progress
```

## List Todo

```bash
    python script.py --list-todo  #list To do tasks
```

## Mark Todo

```bash
    python script.py --mark-todo -i 3 #Mark To do tasks i=flag (index) index = 3
```

## Mark Done

```bash
    python script.py --mark-done -i 3 #mark tasks done with index
```

## Mark In Progress

```bash
    python script.py --mark-in-progress  #mark tasks in progress
```

## Test Script

```bash
   python -m unittest discover
```
## Source Refreneces:
[Task Tracker](https://roadmap.sh/projects/task-tracker)


