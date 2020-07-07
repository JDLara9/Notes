import sqlite3
from sqlite3 import Error
from tkinter import messagebox

conn = None

def create_db_connection():
    try:
        conn = sqlite3.connect('notes.db')
        cursorObj = conn.cursor()
        
        with open('schema.sql') as fp:
            cursorObj.executescript(fp.read())

        conn.commit()
        return conn

    except Error:
        messagebox.showerror('Database Error', 'Something went wrong with setting up the db!')


