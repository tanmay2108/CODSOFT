import tasks
import utility

def main():
    while True:
        print("this is the to do list...")
        print("1. Add Task")
        print("2. View tasks")
        print("3. Mark task as Done")
        print("4. Delete a task")
        print("6. exit")

        choice=input("choose what you want you want to do...(1-3)")
        if choice== '1':
            tasks.addTask()
        elif choice == '2':
            tasks.view_all_tasks()
        elif choice == '3':
            tasks.view_all_tasks()
            task_number= utility.validate_task_number()
            tasks.is_completed(task_number)
        elif choice == '4':
            tasks.view_all_tasks()
            task_number= utility.validate_task_number()
            tasks.delete_task(task_number)
        elif choice == '6':
            print("Make sure you have a Task...")
            break
        else:
            print("invalid input")

main()