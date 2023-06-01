import tkinter as tk


window = tk.Tk()
window.title("Lecture14")
window.geometry('+400+300')

button_1 = tk.Button(window, text="Button1")
button_2 = tk.Button(window, text="Button2")
button_3 = tk.Button(window, text="Button3")

button_1.grid(row=0,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=2,column=0, columnspan=2)


window.mainloop()