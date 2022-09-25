from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title('Clock')

def time():
    timeVar = time.strftime('%H:%M:%S %p')
    clock.config(text = timeVar)
    clock.after(200, time)

clock = Label(master, font=('Calibri', 80), bg='black', fg='cyan')
clock.pack(anchor='center')
time()


master.mainloop()