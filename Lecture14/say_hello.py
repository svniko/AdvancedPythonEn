import tkinter as tk

def Click():
    name = entry.get()
    if not name:
        greetings = "Hello, stranger"
    else:
        entry.delete(0, tk.END)
        greetings = f'Hello, {name}'
    label_hello.config(text=greetings)

window = tk.Tk()
window.title("Say Hello")
window.geometry('+400+300')
window.resizable(False, False)

label_name=tk.Label(text="Enter name")
entry = tk.Entry(font=('Arial', 14))
label_hello = tk.Label(text="Hello, stranger", font=14)
button = tk.Button(window, 
                   text="Press to greet",
                   font=26,
                   command=Click)

label_hello.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0)
entry.grid(row=1, column=1)

button.grid(row=2, column=0, columnspan=2)

window.mainloop()