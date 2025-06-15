import tkinter as t
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC

def on_btn_generate_clicked():
    a = eval(ent_a.get())
    b = eval(ent_b.get())
    n = eval(ent_n.get())
    f = lambda x: eval(ent_func.get())

    plot.clear()
    x = linspace(a, b, 100)
    y = f(x)
    plot.plot(x, y)

    calc_x = linspace(a, b, n + 1)
    calc_y = f(calc_x)

    for i in range(n):
        plot.plot([calc_x[i+1], calc_x[i+1]], [0, calc_y[i+1]], color="gray")

    canvas.draw()

win = t.Tk()
win.title("trapezoidal calc")
win.geometry("720x1280")

fig = Figure(figsize=(5, 4))
plot = fig.add_subplot(111)

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

btn_generate = t.Button(win, text="generate", command=on_btn_generate_clicked)
btn_generate.pack()
win.bind("<Return>", lambda e: on_btn_generate_clicked())

win.mainloop()
