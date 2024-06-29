from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
import sqlite3
import hashlib
import binascii
import os

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha256', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.resizable(0, 0)

        self.canvas1 = tk.Canvas(self.root, width=500, height=300, relief='raised', bg="white")
        self.canvas1.pack()

        self.label1 = tk.Label(self.root, text='Login Page')
        self.label1.config(font=("bold", 18), bg="white")
        self.canvas1.create_window(250, 30, window=self.label1)

        self.label2 = tk.Label(self.root, text='Email :')
        self.label2.config(font=('helvetica', 14), bg="white")
        self.canvas1.create_window(65, 90, window=self.label2)

        self.email = StringVar()
        self.entry1 = tk.Entry(self.root, textvar=self.email, font=(14), borderwidth=2, width=30)
        self.canvas1.create_window(320, 90, window=self.entry1)

        self.label3 = tk.Label(self.root, text='Password :')
        self.label3.config(font=('helvetica', 14), bg="white")
        self.canvas1.create_window(65, 140, window=self.label3)

        self.password = StringVar()
        self.entry2 = tk.Entry(self.root, textvar=self.password, font=(14), borderwidth=2, width=30, show="*")
        self.canvas1.create_window(320, 140, window=self.entry2)

        self.button1 = tk.Button(self.root, text='   Login   ', command=self.login, bg='black', fg='white', font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(250, 190, window=self.button1)

    def login(self):
        email = self.email.get()
        password = self.password.get()
        conn = sqlite3.connect('Form.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Password FROM Student WHERE Email=?', (email,))
        stored_password = cursor.fetchone()
        if stored_password:
            stored_password = stored_password[0]
            if verify_password(stored_password, password):
                showinfo(title="Login", message="Login successful")
            else:
                showinfo(title="Login", message="Invalid password")
        else:
            showinfo(title="Login", message="Email not found")

def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()