#Version 3: GUI Password Manager
import tkinter as tk
import json

class PasswordManager:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        #Create login frame
        self.login_frame = tk.Frame(master)
        self.login_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        #Add login icon to top center of login frame
        self.login_icon = tk.PhotoImage(file="Login Icon.png")
        self.login_icon_label = tk.Label(self.login_frame, image=self.login_icon)
        self.login_icon_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N)

        self.login_account_label = tk.Label(self.login_frame, text="Account:")
        self.login_account_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.login_account_entry = tk.Entry(self.login_frame)
        self.login_account_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.login_password_label = tk.Label(self.login_frame, text="Password:")
        self.login_password_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        self.login_password_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.login_message_label = tk.Label(self.login_frame, text="")
        self.login_message_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        #Create account frame
        self.account_frame = tk.Frame(master)
        self.account_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.account_frame.grid_remove()

        self.account_title_label = tk.Label(self.account_frame, text="Account")
        self.account_title_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.password_title_label = tk.Label(self.account_frame, text="Password")
        self.password_title_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.add_button = tk.Button(self.account_frame, text="Add Password", command=self.add_password)
        self.add_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.get_button = tk.Button(self.account_frame, text="Get Password", command=self.get_password)
        self.get_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.account_message_label = tk.Label(self.account_frame, text="")
        self.account_message_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        #Load passwords from file
        try:
            with open('passwords.json', 'r') as f:
                global passwords
                passwords = json.load(f)
        except FileNotFoundError:
            passwords = {}

    def login(self):
        account = self.login_account_entry.get()
        password = self.login_password_entry.get()
        
        if account == "" or password == "":
            self.login_message_label.config(text="Please enter both account and password.")
        else:
            self.login_frame.grid_remove()
            self.account_frame.grid()
   
        
    def add_password(self):
        account = input("Enter account: ")
        password = input("Enter password: ")
        passwords[account] = password
        self.save_passwords()
        self.account_message_label.config(text="Password added successfully.")
    
    def get_password(self):
        account = input("Enter account: ")
        if account in passwords:
            password = passwords[account]
            self.account_message_label.config(text=f"Password for {account}: {password}")
        else:
            self.account_message_label.config(text=f"No password found for {account}.")
    
    def save_passwords(self):
        with open('passwords.json', 'w') as f:
            json.dump(passwords, f)

root = tk.Tk()
password_manager = PasswordManager(root)
root.mainloop()
