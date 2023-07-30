from tkinter import *
import tkinter.messagebox

window = tkinter.Tk()
window.title("GUI")

def sele():
	selection = "You have selected option "+ str(user.get())
	print(selection)
	
def signin():
	tkinter.messagebox.showinfo("Alert message","This is just an alert message")
	
tkinter.Label(window, text = "Username").grid(row = 0)

username = tkinter.Entry(window).grid(row = 0, column = 1)

user = IntVar()
r1 = Radiobutton(window, text = "student", variable  = user, value = 1, command = sele)
r2 = Radiobutton(window, text = "admin", variable  = user, value = 2, command = sele)
r1.grid(row = 3)
r2.grid(row = 3, column = 1)

tkinter.Checkbutton(window, text = "Kepp me logged in").grid(columnspan = 2)
tkinter.Button(window, text = "sign in", command = signin).grid(row = 5, columnspan = 2)



window.mainloop()
