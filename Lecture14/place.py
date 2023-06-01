import tkinter as tk


window = tk.Tk()
window.title("Lecture14")
window.geometry('300x200+400+300')

button_1 = tk.Button(window, text="Button1")
button_2 = tk.Button(window, text="Button2")
button_3 = tk.Button(window, text="Button3")

button_1.place(x=10, y=10, width=150)
button_2.place(x=50, y=70)
button_3.place(x=100, y=120, height=50)


window.mainloop()