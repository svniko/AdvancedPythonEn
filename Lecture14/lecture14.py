import tkinter as tk
# from tkinter import Button
from tkinter import messagebox

def Click():
    reply = messagebox.askquestion("Quit?", "Are you sure?")
    if reply == 'yes':
        window.destroy();




window = tk.Tk()
window.title("Lecture14")
window.geometry('300x200+400+300')

button = tk.Button(window, 
                   text="Bye!", 
                   padx=50, 
                   pady=50,
                   command=Click)
button.place(x=10, y=10)

window.mainloop()

