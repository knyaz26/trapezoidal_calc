import tkinter as t
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC
from scipy.integrate import quad

def on_btn_generate_clicked():
    a = eval(ent_a.get())
    b = eval(ent_b.get())
    n = eval(ent_n.get())
    f = lambda x: eval(ent_func.get())

    plot.clear()
    x = linspace(a, b, 1000)
    y = f(x)
    plot.plot(x, y)
    plot.plot([a, b], [0, 0], color="red")

    calc_x = linspace(a, b, n + 1)
    calc_y = f(calc_x)

    approx_area = 0.0
    dx = (b - a) / n if n > 0 else 0

    for i in range(n):
        x_i = calc_x[i]
        y_i = calc_y[i]
        x_iplus1 = calc_x[i+1]
        y_iplus1 = calc_y[i+1]

        plot.plot([x_i, x_i], [0, y_i], color="red")
        plot.plot([x_iplus1, x_iplus1], [0, y_iplus1], color="red")

        plot.plot([x_i, x_iplus1], [y_i, y_iplus1], color="red")

        approx_area += (y_i + y_iplus1) * dx / 2

    canvas.draw()

    true_area, _ = quad(f, a, b)
    difference = abs(approx_area - true_area)

    text_out.config(state="normal")
    text_out.delete("1.0", t.END)
    text_out.insert(t.END, f"Trapezoidal Rule: {approx_area:.2f}\n")
    text_out.insert(t.END, f"Integral Rule: {true_area:.2f}\n")
    text_out.insert(t.END, f"Difference: {difference:.2f}\n")
    text_out.config(state="disabled")

win = t.Tk()
win.title("trapezoidal calc")
win.geometry("600x1200")

plt.style.use("grayscale")

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

text_out = t.Text(win, width=40, height=10)
text_out.pack()
text_out.config(state="disabled")

win.mainloop()
