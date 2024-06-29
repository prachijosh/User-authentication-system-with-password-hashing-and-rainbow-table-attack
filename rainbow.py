import tkinter as tk
from tkinter import messagebox
import hashlib

class RainbowTableAttack:
    def __init__(self, root):
        self.root = root
        self.root.title("Rainbow Table Attack")

        # Create input field for hashed password
        self.hashed_password_label = tk.Label(root, text="Enter hashed password:")
        self.hashed_password_label.pack()
        self.hashed_password_entry = tk.Entry(root)
        self.hashed_password_entry.pack()

        # Create button to perform rainbow table attack
        self.attack_button = tk.Button(root, text="Perform Rainbow Table Attack", command=self.perform_attack)
        self.attack_button.pack()

        # Create label to display cracked password
        self.cracked_password_label = tk.Label(root, text="")
        self.cracked_password_label.pack()

    def perform_attack(self):
        hashed_password = self.hashed_password_entry.get()
        rainbow_table = self.create_rainbow_table()
        cracked_password = self.lookup_rainbow_table(hashed_password, rainbow_table)
        if cracked_password:
            self.cracked_password_label.config(text=f"Cracked password: {cracked_password}")
        else:
            self.cracked_password_label.config(text="Password not found in rainbow table")

    def create_rainbow_table(self):
        # Create a sample rainbow table with 10 common passwords
        rainbow_table = {
            "5f4dcc3b5aa765d61d8327deb882cf99": "password123",
            "7c6a180b36896a0a8c02787eeafb0e4c": "iloveyou",
            "d7a8fbb307d7809469ca9abcb0082e4f": "dragonball",
            "1a1dc91c907325c69271ddf0c944bc72": "letmein",
            "5baa61e4c9b93f3f0682250b6cf8331b7": "monkey",
            "e10adc3949ba59abbe56e057f20f883e": "football",
            "9f86d081884c7d659a2feaa0c55ad015": "baseball",
            "2ef7bde608ce5404e97d5f042f95f89f": "sunshine",
            "4b227777d4dd1fc61c6f884f48641d02": "princess",
            "8d969eef6ecad3c29a3a629280e686cf": "qwerty",
            "96268c9d77693511508d09f6d379bb6a993b0cc1df871264f0a3ca8801cbdc5cc7718bf840803e05460649cea0230c3880de584cbf54644e0a16d1a19457f750":"anaya@123",
            "28379410955e76a65df41d6531de9ce349df2290bf3782c968e914d4a48ac88a60698af3ba69c37f0c32fe461c4432294581701bf0bd04c1d6967448280958fe":"pass@123"
        }
        return rainbow_table

    def lookup_rainbow_table(self, hashed_password, rainbow_table):
        for hash_value, password in rainbow_table.items():
            if hash_value == hashed_password:
                return password
        return None

root = tk.Tk()
app = RainbowTableAttack(root)
root.mainloop()