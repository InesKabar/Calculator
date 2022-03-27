import tkinter as tk

window = tk.Tk()
window.geometry("330x430+500+500")
window.resizable(0, 0)
window.title("Calculator")
data = tk.StringVar()
number = ""


def button_click(n):
    global number
    number += str(n)
    global data
    data.set(number)


def clear_click():
    global number, data
    number = ""
    data.set(number)


def equal_input():
    global number
    sum = str((eval(number)))
    data.set(sum)
    number = ""


e = tk.Entry(window, fg='Orange', width=10, font=("Helvetica", 40, 'bold'), bg='white', bd=20,
             justify='right', textvariable=data).grid(columnspan=180)

btn1 = tk.Button(window, text='1', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(1)).grid(row=1, column=0)

btn2 = tk.Button(window, text='2', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(2)).grid(row=1, column=1)

btn3 = tk.Button(window, text='3', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(3)).grid(row=1, column=2)

add = tk.Button(window, text='+', fg='White', bg='Orange', width=3, bd=5,
                font=("Helvetica", 27, 'bold'), command=lambda: button_click("+")).grid(row=1, column=3)

btn4 = tk.Button(window, text='4', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(4)).grid(row=2, column=0)

btn5 = tk.Button(window, text='5', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(5)).grid(row=2, column=1)

btn6 = tk.Button(window, text='6', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(6)).grid(row=2, column=2)

sub = tk.Button(window, text='-', fg='White', bg='Orange', width=3, bd=5,
                font=("Helvetica", 27, 'bold'), command=lambda: button_click("-")).grid(row=2, column=3)

btn7 = tk.Button(window, text='7', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(7)).grid(row=3, column=0)

btn8 = tk.Button(window, text='8', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(8)).grid(row=3, column=1)

btn9 = tk.Button(window, text='9', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(9)).grid(row=3, column=2)

mul = tk.Button(window, text='*', fg='White', bg='Orange', width=3, bd=5,
                font=("Helvetica", 27, 'bold'), command=lambda: button_click("*")).grid(row=3, column=3)

btn0 = tk.Button(window, text='0', fg='Orange', bg='White', width=3, bd=5,
                 font=("Helvetica", 27, 'bold'), command=lambda: button_click(0)).grid(row=4, column=0)

division = tk.Button(window, text='/', fg='White', bg='Orange', width=3, bd=5,
                     font=("Helvetica", 27, 'bold'), command=lambda: button_click("/")).grid(row=4, column=3)

clear = tk.Button(window, text='C', fg='White', bg='orange', width=3, bd=5,
                  font=("Helvetica", 27, 'bold'), command=lambda: clear_click()).grid(row=4, column=1)

equals = tk.Button(window, text='=', fg='White', bg='Orange', width=3, bd=5,
                   font=("Helvetica", 27, 'bold'), command=lambda: equal_input()).grid(row=4, column=2)

window.mainloop()