from tkinter import *
from tkinter import ttk

def greet(*args):
    var_two.set("hello")

def chk_feeling(*args):
    var_two.set(chk_var.get())

def chg_pet(*args):
    var_two.set(radio_var.get())

def combo_chg(*args):
    var_two.set(combox_var.get())


root = Tk()
root.title("Widgets")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

var_one = StringVar()

label_one = ttk.Label(frame, text="Data: ")
label_one.grid(column=1, row=1, sticky=(W, E))
label_one["textvariable"] = var_one
var_one.set('Data ')

var_two = StringVar()

entry_one = ttk.Entry(frame, width=10, textvariable=var_two)
entry_one.grid(column=2, row=1, sticky=(W, E))
var_two.set(var_one.get())

btn = ttk.Button(frame, text="click", command=greet)
btn.grid(column=3, row=1, sticky=(W, E))

chk_var = StringVar()
chk_btn = ttk.Checkbutton(frame, text="feeling", command=chk_feeling, variable=chk_var, onvalue="happy",
                          offvalue="sad")
chk_btn.grid(column=1, row=2, sticky=(W, E))

radio_var = StringVar()
radio_cat_btn = ttk.Radiobutton(frame, text="cat", variable=radio_var, value="cat", command=chg_pet)
radio_dog_btn = ttk.Radiobutton(frame, text="dog", variable=radio_var, value="dog", command=chg_pet)

radio_cat_btn.grid(column=2, row=3, sticky=(W, E))
radio_dog_btn.grid(column=3, row=3, sticky=(W, E))

radio_label = ttk.Label(frame, text="Fav pet: ")
radio_label.grid(column=1, row=3, sticky=(W, E))

combox_var = StringVar()
combo_box = ttk.Combobox(frame, textvariable=combox_var)
combox_label = ttk.Label(frame, text="Size")
combox_label.grid(column=1, row=4, sticky=(W, E))
combo_box["values"] = ("small", "medium", "large")
combo_box.grid(column=2, row=4, sticky=(W, E))
combo_box.bind("<<ComboboxSelected>>", combo_chg)

root.mainloop()
