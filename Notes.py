from tkinter import *

gui = Tk(className = 'Notes')
gui.geometry("800x685")
gui['background']='#1e2024'


"""
label_1 = Label(gui, text="Name:")
label_2 = Label(gui, text="Password:")
entry_1 = Entry(gui)
entry_2 = Entry(gui)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(gui, text="Keep me logged in")
c.grid(columnspan=2)
"""

"""topFrame = Frame(gui)
topFrame.pack()
bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM)"""



#Create labels like in a graph
"""
one = Label(gui, text="One", bg="red", fg="white")
one.pack()
two = Label(gui, text="two", bg="red", fg="white")
#fill=X makes it scalable along the X axis
two.pack(fill=X)
three = Label(gui, text="two", bg="red", fg="white")
three.pack(side=LEFT, fill=Y)
"""


#To create buttons
"""
button1 = Button(topFrame, text="Save", fg = "red")
button2 = Button(topFrame, text="Open", fg = "blue")
button3 = Button(topFrame, text="Button 3", fg = "green")
button4 = Button(topFrame, text="Button 4", fg = "yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
"""

gui.mainloop()
