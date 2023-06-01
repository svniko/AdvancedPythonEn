import tkinter as tk
from tkinter import ttk

def Click():
    
    name = entry.get()
    if not name:
        greetings = 'Hello, stranger'
    else:
        entry.delete(0, tk.END)
        greetings = f'Hello, {name}'
    label_hello.config(text=greetings)

window = tk.Tk()
window.geometry("+300+400")
window.title("Say Hello")
window.attributes("-alpha", 0.5)
window.attributes("-toolwindow", True)
 

window.resizable(False,False)
label_name = ttk.Label(text="Enter name")
entry = ttk.Entry(font=("Arial", 14))
label_hello = ttk.Label(text = 'Hello, stranger', font=14 )
button = tk.Button(window, text="Press to greet",
                   font = 26,
                   command=Click)

label_hello.grid(row=0, column=0, columnspan = 2)
label_name.grid(row=1, column=0)
entry.grid(row=1, column = 1)

button.grid(row=2, column=0, columnspan = 2)

window.mainloop()


