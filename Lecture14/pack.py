import tkinter as tk


window = tk.Tk()
window.title("Lecture14")
window.geometry('+400+300')

button_1 = tk.Button(window, 
                    text="Button1", 
                    bg='yellow', 
                    fg='#ff0000',
                    activeforeground='#0000FF',
                    activebackground='#FFFFFF')
button_2 = tk.Button(window, text="Button2")
button_3 = tk.Button(window, text="Button3")

button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()


window.mainloop()