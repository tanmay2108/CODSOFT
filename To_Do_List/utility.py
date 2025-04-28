def validate_task_number():
    while True:
        try:
            task_number = int(input("Enter the task number: "))
            if task_number <= 0:
                raise ValueError
            return task_number
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

