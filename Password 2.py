#Version 2: Password Manager with Improved Functionality

#Creating an empty dictionary to store account name and password
passwords = {}

#Using 3 functions like adding passwords to account and asking to get password from dictionary
def add_password(account, password):
    #Check if account name already exists in the dictionary
    if account in passwords:
        print(f"Account name '{account}' already exists.")
    else:
        passwords[account] = password
        print(f"Password added for account '{account}'.")

def get_password(account):
    password = passwords.get(account, None)
    if password:
        print(f"Password for account '{account}': {password}")
    else:
        print(f"No such account name found '{account}'.")

def main():
    while True:
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            add_password(account, password)
        elif choice == "2":
            account = input("Enter account name: ")
            get_password(account)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
