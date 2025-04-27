tasks=[]

def addTask():
    task= input("Enter Your task. ")
    tasks.append({"task":task, "done":False})
    print("Tsak added.")

def view_task():
    if not tasks:
        print("No task found ")
        return
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

def view_all_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx + 1}. {task['task']} - {status}")
        print()

def is_completed(task_number):
    try:
        task = tasks[task_number - 1]
        task["done"] = True
        print(f"Task '{task['task']}' marked as completed!\n")
    except IndexError:
        print("Invalid task number.\n")