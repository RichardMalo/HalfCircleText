import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog

def create_sentence_plot(sentence="a year from now you will wish you started today", bg_color='black', txt_color='white', line_color='white', capitalize=False):
    if capitalize:
        sentence = sentence.title()
    words = sentence.split()

    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.set_aspect('equal')

    n = len(words)

    x = np.linspace(0, 2*n, n)
    y = [0] * n

    radius = abs(x[-2] - x[0]) / 2

    for i in range(n-1):
        ax.text(x[i], y[i], words[i], color=txt_color, ha='center')

    ax.text(radius, -radius - 1, words[-1], color=txt_color, ha='center')

    for i in range(1, n-1):
        radius_i = abs(x[i] - x[0]) / 2
        arc = Arc((radius_i, 0.5), 2*radius_i, 2*radius_i,
                  theta1=0, theta2=180, edgecolor=line_color, lw=2)
        ax.add_patch(arc)

    start_arc_1, end_arc_1 = 180, 270
    start_arc_2, end_arc_2 = 270, 360

    arc_1 = Arc((radius, -0.25), 2*radius, 2*radius,
                theta1=start_arc_1, theta2=end_arc_1, edgecolor=bg_color, lw=2)
    arc_2 = Arc((radius, -0.25), 2*radius, 2*radius,
                theta1=start_arc_2, theta2=end_arc_2, edgecolor=line_color, lw=2)

    ax.add_patch(arc_1)
    ax.add_patch(arc_2)

    ax.axis('off')

    ax.set_xlim(-1, 2*n+1)
    ax.set_ylim(-radius-2, radius+2)

    return fig

def get_sentence():
    def on_plot_closing(event):
        root.deiconify()

    def submit():
        sentence = entry.get()
        bg_color = bg_color_var.get()
        txt_color = txt_color_var.get()
        line_color = line_color_var.get()
        capitalize = var_capitalize.get()
        root.iconify()
        if sentence:
            fig = create_sentence_plot(sentence, bg_color, txt_color, line_color, capitalize)
        else:
            fig = create_sentence_plot(bg_color=bg_color, txt_color=txt_color, line_color=line_color, capitalize=capitalize)

        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialdir=".")
        if file_path:
            fig.savefig(file_path)

    def clear():
        entry.delete(0, 'end')

    root = tk.Tk()
    tk.Label(root, text="Enter a sentence:").pack()

    entry = tk.Entry(root, width=60)
    entry.insert(0, "a year from now you will wish you started today")
    entry.pack()

    tk.Button(root, text="Clear", command=clear).pack()

    colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple', 'aqua', 'magenta', 
    'lime', 'teal', 'maroon', 'navy', 'olive', 'silver', 'gray', 'pink', 'cyan', 'orange', 'brown', 
    'aliceblue', 'antiquewhite', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 
    'blueviolet', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 
    'cornsilk', 'crimson', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 
    'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 
    'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 
    'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 
    'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 
    'goldenrod', 'greenyellow']

    tk.Label(root, text="Select Background Color").pack()
    bg_color_var = tk.StringVar(root)
    bg_color_var.set('black')
    bg_color_option = ttk.Combobox(root, textvariable=bg_color_var, values=colors, width=58)
    bg_color_option.pack()

    tk.Label(root, text="Select Text Color").pack()
    txt_color_var = tk.StringVar(root)
    txt_color_var.set('white')
    txt_color_option = ttk.Combobox(root, textvariable=txt_color_var, values=colors, width=58)
    txt_color_option.pack()

    tk.Label(root, text="Select Line Color").pack()
    line_color_var = tk.StringVar(root)
    line_color_var.set('white')
    line_color_option = ttk.Combobox(root, textvariable=line_color_var, values=colors, width=58)
    line_color_option.pack()

    var_capitalize = tk.BooleanVar()
    var_capitalize.set(False)
    tk.Label(root, text="Capitalize first letter of each word").pack()
    chk_capitalize = tk.Checkbutton(root, variable=var_capitalize)
    chk_capitalize.pack()

    tk.Button(root, text="Submit", command=submit).pack()
    root.mainloop()

get_sentence()