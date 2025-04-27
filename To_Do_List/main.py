import tasks
import utility

def main():
    while True:
        print("this is the to do list...")
        print("1. Add Task")
        print("2. View task")
        print("3. Mark task as Done")
        print("6. exit")

        choice=input("choose what you want you want to do...(1-3)")
        if choice== '1':
            tasks.addTask()
        elif choice == '2':
            tasks.view_task()
        elif choice == '3':
            tasks.view_all_tasks()
            task_number= utility.validate_task_number()
            tasks.is_completed(task_number)
        elif choice == '6':
            print("better luck next time...")
            break
        else:
            print("invalid input")

main()