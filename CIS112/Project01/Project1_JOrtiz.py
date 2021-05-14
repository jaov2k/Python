# Jose Ortiz
# 05-12-2021
# CIS112 - Spring 2021
# Assignment Project 1
#
# PURPOSE:  Python program to create a simple GUI
#           calculator using Tkinter


# ------------------ START ------------------ #

#Tkinter module for use with GUI applications
import tkinter as tk

def clearPress():
    '''Resets the entry field to blank'''
    global tempString
    tempString = ""
    equation.set("")

def equalPress():
    '''Evaluates tempString and updates the entry field with the total'''
    try:
        global tempString
        total = str(eval(tempString))
        equation.set(total)
        tempString = ""
    except:
        equation.set(" error ")
        tempString = ""

def buttonPress(num):
    '''Appends the passed value to the current expersion contents.'''
    global tempString
    tempString = tempString + str(num)
    equation.set(tempString)    

#Main program
if __name__ == "__main__":
    #Calculator layout and action definitions

    #Setup the base of the calculator
    calc = tk.Tk()
    calc.configure(background='ghost white')
    calc.title("Project 1")
    calc.geometry("433x245")

    #Temporary string variable for assembling and evaluating math operations.
    tempString = ""

    #StingVar Object for updating the Entry type field object.
    equation = tk.StringVar()

    #Setup of the entry field
    expression_field = tk.Entry(calc, textvariable=equation, background='old lace', font='Helvetica', justify="right")
    expression_field.grid(columnspan=4, ipadx=100,ipady=10)

    #First row of buttons: row=2
    button1 = tk.Button(calc, text='1', fg='black', bg='light grey', command=lambda: buttonPress(1), height=2, width=14)
    button1.grid(row=2, column=0)
    button2 = tk.Button(calc, text='2', fg='black', bg='light grey', command=lambda: buttonPress(2), height=2, width=14)
    button2.grid(row=2, column=1)
    button3 = tk.Button(calc, text='3', fg='black', bg='light grey', command=lambda: buttonPress(3), height=2, width=14)
    button3.grid(row=2, column=2)    
    plus = tk.Button(calc, text='+', fg='black', bg='light grey', command=lambda: buttonPress("+"), height=2, width=14)
    plus.grid(row=2, column=3)

    #Second row of buttons: row=3
    button4 = tk.Button(calc, text='4', fg='black', bg='light grey', command=lambda: buttonPress(4), height=2, width=14)
    button4.grid(row=3, column=0)
    button5 = tk.Button(calc, text='5', fg='black', bg='light grey', command=lambda: buttonPress(5), height=2, width=14)
    button5.grid(row=3, column=1)
    button6 = tk.Button(calc, text='6', fg='black', bg='light grey', command=lambda: buttonPress(6), height=2, width=14)
    button6.grid(row=3, column=2)
    minus = tk.Button(calc, text='-', fg='black', bg='light grey', command=lambda: buttonPress("-"), height=2, width=14)
    minus.grid(row=3, column=3)

    #Third row of buttons: row=4
    button7 = tk.Button(calc, text=' 7 ', fg='black', bg='light grey', command=lambda: buttonPress(7), height=2, width=14)
    button7.grid(row=4, column=0)
    button8 = tk.Button(calc, text=' 8 ', fg='black', bg='light grey', command=lambda: buttonPress(8), height=2, width=14)
    button8.grid(row=4, column=1)
    button9 = tk.Button(calc, text=' 9 ', fg='black', bg='light grey', command=lambda: buttonPress(9), height=2, width=14)
    button9.grid(row=4, column=2)
    multiply = tk.Button(calc, text=' * ', fg='black', bg='light grey', command=lambda: buttonPress("*"), height=2, width=14)
    multiply.grid(row=4, column=3)
    
    #Fourth row of buttons: row=5
    button0 = tk.Button(calc, text=' 0 ', fg='black', bg='light grey', command=lambda: buttonPress(0), height=2, width=29)
    button0.grid(row=5, column=0, columnspan = 2)	
    Decimal = tk.Button(calc, text='.', fg='black', bg='light grey', command=lambda: buttonPress('.'), height=2, width=14)
    Decimal.grid(row=5, column=2)
    divide = tk.Button(calc, text=' / ', fg='black', bg='light grey', command=lambda: buttonPress("/"), height=2, width=14)
    divide.grid(row=5, column=3)

    #Fifth row of buttons: row=6
    equal = tk.Button(calc, text=' = ', fg='black', bg='light grey', command=equalPress, height=2, width=45)
    equal.grid(row=6, column=0,columnspan = 3)
    clear = tk.Button(calc, text='Clear', fg='black', bg='light grey', command=clearPress, height=2, width=14)
    clear.grid(row=6, column='3')

    #Calls the application
    calc.mainloop()

# ------------------ END ------------------ #