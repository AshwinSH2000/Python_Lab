from tkinter import *
import tkinter.messagebox

window = tkinter.Tk()
window.title("CALCULATOR")

expression = ""
equation = StringVar() 	
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
	
tkinter.Label(window, text = "").grid(row = 0)

username = tkinter.Entry(window).grid(row = 0, column = 1)

user = IntVar()
num = IntVar()
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression)
    print(expression)
def equalpress(): 
    
    try: 
  
        global expression        
        total = str(eval(expression))  
        equation.set(total)
        print(equation)
        expression = ""     
    except: 
        equation.set(" error ") 
        expression = "" 
  
  

b1=tkinter.Button(window, text = "1", width = 5, command =lambda: press(1)).grid(row = 5, column = 0)
b2=tkinter.Button(window, text = "2", width = 5,command = lambda: press(2)).grid(row = 5, column = 1)
b3=tkinter.Button(window, text = "3", width = 5,command = lambda: press(3)).grid(row = 5, column = 2)
b4=tkinter.Button(window, text = "4", width = 5,command = lambda: press(4)).grid(row = 6, column = 0)
b5=tkinter.Button(window, text = "5", width = 5,command = lambda: press(5)).grid(row = 6, column = 1)
b6=tkinter.Button(window, text = "6", width = 5,command = lambda: press(6)).grid(row = 6, column = 2)
b7=tkinter.Button(window, text = "7", width = 5,command = lambda: press(7)).grid(row = 7, column = 0)
b8=tkinter.Button(window, text = "8", width = 5,command = lambda: press(8)).grid(row = 7, column = 1)
b9=tkinter.Button(window, text = "9", width = 5,command = lambda: press(9)).grid(row = 7, column = 2)
b0=tkinter.Button(window, text = "0", width = 5,command = lambda: press(0)).grid(row = 8, column = 1)
bplus=tkinter.Button(window, text = "+", width = 5,command = lambda: press("+")).grid(row = 8)
bminus=tkinter.Button(window, text = "-", width = 5,command = lambda:press("-")).grid(row = 8, column = 2)
bby=tkinter.Button(window, text = "/", width = 5,command = lambda:press("/")).grid(row = 9)
binto=tkinter.Button(window, text = "*", width = 5,command = lambda:press("*")).grid(row = 9, column = 1)
bequal=tkinter.Button(window, text = "=", width = 5,command = lambda:equalpress()).grid(row = 9, column = 2)



window.mainloop()
