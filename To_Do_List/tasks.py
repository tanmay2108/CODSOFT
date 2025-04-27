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