# import everything from tkinter
from tkinter import *
# import the themed widget set
from tkinter import ttk

# create the main window object
window = Tk()
# add a title to the window
window.title("Hello, world")


def get_res(*args):
    try:
        str_one_val = str_one.get()
        print(str_one_val)
        str_two_val = str_two.get()
        print(type(str_two))
        res.set(f"{str_one_val}, {str_two_val}")
    except ValueError:
        pass


# create a frame that will surround the widgets
frame = ttk.Frame(window, padding="10 10 10 10")

# create layout grid
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# create variables
str_one = StringVar()
str_two = StringVar()
res = StringVar()

# create entries and button
str_one_entry = ttk.Entry(frame, width=10, textvariable=str_one)
str_one_entry.grid(column=1, row=1, sticky=(W, E))

ttk.Label(frame, text="+", anchor="center").grid(column=2, row=1, sticky=(W, E))

str_two_entry = ttk.Entry(frame, width=10, textvariable=str_two)
str_two_entry.grid(column=3, row=1, sticky=(W, E))

ttk.Button(frame, text="enter", command=get_res).grid(column=2, row=2, sticky=(W, E))

res_entry = ttk.Entry(frame, width=10, textvariable=res)
res_entry.grid(column=2, row=3, sticky=(W, E))

# focus on the first entry
str_one_entry.focus()

# bind return key to the function
window.bind("<Return>", get_res)

# create the loop that listens for events
window.mainloop()
