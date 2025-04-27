import tasks

def main():
    while True:
        print("this is the to do list...")
        print("1. Add Task")
        print("2. View task")
        print("3. exit")

        choice=input("choose what you want you want to do...(1-3)")
        if choice== '1':
            tasks.addTask()
        elif choice == '2':
            tasks.view_task()
        elif choice == '3':
            print("better luck next time...")
            break
        else:
            print("invalid input")

main()