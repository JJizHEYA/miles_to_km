
from tkinter import *

windows = Tk()
windows.minsize(200, 100)
windows.title("Miles to Km converter")
windows.config(padx=40, pady=40)

empty = Label(windows, text=" ", font=("aerial", 10, "bold"))
empty.grid(column=0, row=0)

miles = Entry()
miles.grid(column=2, row=1)

Miles = Label(windows, text="Miles", font=("aerial", 10, "bold"))
Miles.grid(column=3, row=1)

is_equal_to = Label(windows, text="is equal to", font=("aerial", 10, "bold"))
is_equal_to.grid(column=0, row=2)

Km = Label(windows, text="Km", font=("aerial", 10, "bold"))
Km.grid(column=3, row=2)


def button_pressed():
    ans = int(miles.get())
    ans *= 1.609344
    final_ans = Label(windows, text=f"{round(ans,2)}", font=("aerial", 10, "bold"))
    final_ans.grid(column=2, row=2)


calculate = Button(text="calculate", command=button_pressed)
calculate.grid(column=2, row=3)


windows.mainloop()