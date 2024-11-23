# Task-Tracker-Cli

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
