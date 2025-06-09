import tkinter as tk
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

window = tk.Tk()
window.geometry("800x800")
window.title("Binomial Distribution")

def calculate():
    global sum
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    a = int(a)
    b = float(b)
    c = int(c)
    sum = random.binomial(n = a, p = b, size = c)
    label_show.configure(text = f"{sum}")

def plot():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    a = int(a)
    b = float(b)
    c = int(c)
    sns.displot(random.binomial(n = a, p = b, size = c))
    plt.show()


label_title = tk.Label(text = "Binomial Distribution", font = ("Comic Sans MS", 20))
label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

label_trails = tk.Label(text = "Number of trials", font = ("Comic Sans MS", 20))
label_trails.place(relx = 0.3, rely = 0.45, anchor = "center")

entry1 = tk.Entry(font = ("Comic Sans MS", 20))
entry1.place(relx = 0.3, rely = 0.5, anchor = "center")

label_prob = tk.Label(text = "The propebility", font = ("Comic Sans MS", 20))
label_prob.place(relx = 0.5, rely = 0.45, anchor = "center")

entry2 = tk.Entry(font = ("Comic Sans MS", 20))
entry2.place(relx = 0.5, rely = 0.5, anchor = "center")

label_size = tk.Label(text = "The number of attempts", font = ("Comic Sans MS", 20))
label_size.place(relx = 0.7, rely = 0.45, anchor = "center")

entry3 = tk.Entry(font = ("Comic Sans MS", 20))
entry3.place(relx = 0.7, rely = 0.5, anchor = "center")

button_calculate = tk.Button(text = "Calculate", font = ("Comic Sans MS", 20), command = calculate)
button_calculate.place(relx = 0.5, rely = 0.6, anchor = "center")

button_plot = tk.Button(text = "Plot", font = ("Comic Sans MS", 20), command = plot)
button_plot.place(relx = 0.5, rely = 0.7, anchor = "center")

label_show = tk.Label(text  = "", font = ("Comic Sans MS", 20))
label_show.place(relx = 0.7, rely = 0.7, anchor = "center")


window.mainloop()
