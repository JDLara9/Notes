import tkinter as tk
from tkinter import messagebox
import sys

# We can make a default font to be used here or be able to change it later
# by going to settings in future sprint
DEFAULT_FONT = ('Verdana', 12)

class App:
    def __init__(self):
        self.root_window = tk.Tk(className = 'Notes')
        self.root_window.geometry("800x685")
        self.root_window['background']='#1e2024'
        self.show()

    def show(self):
        topFrame = tk.Frame(self.root_window)
        topFrame.pack()
        bottomFrame = tk.Frame(self.root_window)
        bottomFrame.pack(side=tk.BOTTOM)


        #To create buttons
        button1 = tk.Button(topFrame, text="Save", fg = "red")
        button2 = tk.Button(topFrame, text="Open", fg = "blue")
        button3 = tk.Button(topFrame, text="Button 3", fg = "green")
        button4 = tk.Button(topFrame, text="Button 4", fg = "yellow")

        button1.pack(side=tk.LEFT)
        button2.pack(side=tk.LEFT)
        button3.pack(side=tk.LEFT)
        button4.pack(side=tk.LEFT)

        messagebox.showinfo("Welcome to Notes", "Please feel free to type in your credit card information!")

    def start(self):
        self.root_window.mainloop()

if __name__ == '__main__':
    App().start()
