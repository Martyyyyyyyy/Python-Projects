from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title('Clock')

def get_time():
    timeVar = time.strftime('%I:%M:%S %p')
    clock.config(text = timeVar)
    clock.after(200, get_time)

clock = Label(master, font=('Calibri', 80), bg='black', fg='cyan')
clock.pack(anchor='center')
get_time()


master.mainloop()