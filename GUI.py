import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("200x200")
Label(window, text="My Simple App").grid(row=0, column=0)
Entry(window).grid(row=1,column=0)

window.mainloop()