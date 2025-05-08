import random
import string

def new_password(length):
    characters=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choices(characters,k=length))
    return password
  
def main():
    print("This is the new Password Generator...")
    length=int(input("Length of the password= "))
    if length>0:
        password=new_password(length)
        print(f"The new Generated password is ({password})")
    else:
        print("Enter a valid Length")
    
main()
