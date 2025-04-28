def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error, can't divide by zero."
    return a/b

def main():
    print("This is the Python Calculator. ")
    print("Let's Do some Basic Maths...")
    while True:
        
        print("Select the operation. ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice= input("\nEnter your choice...(1 to 5)")

        if choice in ['1','2','3','4']:
            try:
                num1= int(input("Enter 1st Number. "))
                num2= int(input("Enter 2nd Number. "))
            except ValueError:
                print("Invalid Input given, Please enter numbers only. ")

        if choice == '1':
            print(f"Result after addtion: {add(num1,num2)}")
        if choice == '2':
            print(f"Result after subtraction: {sub(num1,num2)}")
        if choice == '3':
            print(f"Result after multiplying: {multiply(num1,num2)}")
        if choice == '4':
            print(f"Result after division: {divide(num1,num2)}")
        elif choice == '5':
            print("Exit Operation...Goodbye")
            break
        else:
            print("  Please choose specified choices! ")

main()