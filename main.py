import tkinter as tk
from time import strftime

def time():
    string = strftime(" %I : %M : %S %p\n %d %B %Y")
    label.config(text = string)
    label.after(1000,time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root,font = ("Geogria",50),bg = "black",fg = "white")
label.pack(anchor = "center")

time()

root.mainloop()
