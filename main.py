import tkinter as t
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC

win = t.Tk()
win.title("trapezoidal calc")
win.geometry("720x1280")

x = np.linspace(0, 10, 100)
y = x**2 + 5

fig = Figure(figsize=(5, 4))
plot = fig.add_subplot(111)
plot.plot(x, y)

canvas = FC(fig, master=win)
canvas.get_tk_widget().pack()

hbox = t.Frame(win)
hbox.pack()

vbox_func = t.Frame(hbox)
vbox_func.pack(side="left")
lbl_func = t.Label(vbox_func, text="function")
lbl_func.pack()
ent_func = t.Entry(vbox_func)
ent_func.pack()

vbox_a = t.Frame(hbox)
vbox_a.pack(side="left")
lbl_a = t.Label(vbox_a, text="a")
lbl_a.pack()
ent_a = t.Entry(vbox_a)
ent_a.pack()

vbox_b = t.Frame(hbox)
vbox_b.pack(side="left")
lbl_b = t.Label(vbox_b, text="b")
lbl_b.pack()
ent_b = t.Entry(vbox_b)
ent_b.pack()

vbox_n = t.Frame(hbox)
vbox_n.pack(side="left")
lbl_n = t.Label(vbox_n, text="n")
lbl_n.pack()
ent_n = t.Entry(vbox_n)
ent_n.pack()

btn_generate = t.Button(win, text="generate")
btn_generate.config(command=lambda: canvas.draw())
btn_generate.pack()

win.mainloop()
