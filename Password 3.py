#Version 3: GUI Password Manager

import tkinter as tk
import json

class PasswordManager:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        #Create account label and entry widget
        self.account_label = tk.Label(master, text="Account:")
        self.account_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.account_entry = tk.Entry(master)
        self.account_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        #Create password label and entry widget
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        #Create add password button
        self.add_button = tk.Button(master, text="Add Password", command=self.add_password)
        self.add_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        #Create get password button
        self.get_button = tk.Button(master, text="Get Password", command=self.get_password)
        self.get_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        #Create message label
        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        #Load passwords from file
        try:
            with open('passwords.json', 'r') as f:
                global passwords
                passwords = json.load(f)
        except FileNotFoundError:
            passwords = {}

    def add_password(self):
        account = self.account_entry.get()
        password = self.password_entry.get()

        if account == "":
            self.message_label.config(text="Please enter an account name.")
        elif account in passwords:
            self.message_label.config(text=f"Account name '{account}' already exists.")
        else:
            passwords[account] = password
            with open('passwords.json', 'w') as f:
                json.dump(passwords, f)
            self.message_label.config(text=f"Password added for account '{account}'.")
            self.account_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

    def get_password(self):
        account = self.account_entry.get()

        if account == "":
            self.message_label.config(text="Please enter an account name.")
        elif account not in passwords:
            self.message_label.config(text=f"No password found for account '{account}'.")
        else:
            password = passwords[account]
            self.message_label.config(text=f"Password for account '{account}': {password}")
            self.account_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
