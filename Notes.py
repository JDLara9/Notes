import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
import db
import webbrowser

 # We can make a default font to be used here or be able to change it later
 # by going to settings in future sprint
DEFAULT_FONT = ('Verdana', 12)
conn = db.create_db_connection()

class App:
    def __init__(self):
        super().__init__()
        self.root_window = tk.Tk()
        self.root_window.title('NotePad')
        self.root_window.geometry("800x685")
        self.root_window['background'] = '#1e2024'
        
        self.show()
        self.setupUI()

    def setupUI(self):
        menuBar = tk.Menu(self.root_window)
        self.root_window.config(menu=menuBar)

        # Menu for File
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Sign up", command=self.create)
        fileMenu.add_command(label="Sign in", command=self.login)
        fileMenu.add_separator()
        fileMenu.add_command(label="New", command=self.newNote)
        fileMenu.add_command(label="Open", command=self.openNote)
        fileMenu.add_command(label="Save", command=self.saveNote)
        fileMenu.add_command(label="Save as...", command=self.saveAsNote)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exitNote)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Menu for Edit
        editMenu = tk.Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Copy", command=self.onCopy)
        menuBar.add_cascade(label="Edit", menu=editMenu)

        # Menu for Contact
        contactMenu = tk.Menu(menuBar, tearoff=0)
        contactMenu.add_command(label="Github", command=self.onGithub)
        menuBar.add_cascade(label="Contact", menu=contactMenu)

    def show(self):
        topFrame = tk.Frame(self.root_window)
        topFrame.pack()
        bottomFrame = tk.Frame(self.root_window)
        bottomFrame.pack(side=tk.BOTTOM)
        text = tk.Text(self.root_window, fg = "gray", bg = '#1e2024')
        text.config(font=DEFAULT_FONT, fg='white')
        text.pack(expand=True, fill= BOTH)

    def create(self):
        # You can create your db account so you can store notes offline
        messagebox.showwarning('Warning', 'Work in progress...')
        conn.execute('INSERT INTO user (username, password) VALUES (?,?)', ("Mario", "note123"))
        conn.commit()
        messagebox.showinfo('Database', 'You have created account')

    def login(self):
        # You can login to your db account so you can store notes offline
        messagebox.showwarning('Warning', 'Work in progress...')

    def newNote(self):
        # Thinking this opens up another NotePad window
        tk.messagebox.showwarning('Warning', 'Work in progress...')

    def openNote(self):
        # This will open an existing note, once we have a DB tho
        messagebox.showwarning('Warning', 'Work in progress...')

    def saveNote(self):
        # Save note locally
        messagebox.showwarning('Warning', 'Work in progress...')

    def saveAsNote(self):
        # Save note with custom name either locally or in db once setup
        messagebox.showwarning('Warning', 'Work in progress...')

    def exitNote(self):
        if conn:
            conn.close() #close db connection

        self.root_window.quit()

    def onCopy(self):
        # This will do a copy of highlighted area
        messagebox.showwarning('Warning', 'Work in progress...')

    def onGithub(self):
        webbrowser.open('https://github.com/JDLara9/Notes')

    def start(self):
        self.root_window.mainloop()

if __name__ == '__main__':
    App().start()