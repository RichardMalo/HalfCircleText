import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
matplotlib.use("TkAgg")  # Use this backend for compatibility with tkinter and the window manager.
import tkinter as tk
from tkinter import ttk

def plot_triangles(sentence, bg_color='black', txt_color='white', line_color='white', filename='outputv1.jpg'):
    words = sentence.split()
    fig, ax = plt.subplots(figsize=(10, 10))  # Increase the figure size

    # hide axes and ticks
    ax.axis('off')

    # Set the color of the figure
    fig.patch.set_facecolor(bg_color)

    # Set the vertical offset for the center of the triangles and the text
    text_offset = 0.1

    for i, word in enumerate(words):
        # Place text
        ax.text(i, -text_offset, word, ha='center', va='center', color=txt_color)

    # Create triangles from the first word to every other word
    for i in range(1, len(words)):
        line1 = patches.ConnectionPatch((0, text_offset), (i/2, i/2 + text_offset), 'data', 'data', edgecolor=line_color)
        ax.add_patch(line1)
        line2 = patches.ConnectionPatch((i/2, i/2 + text_offset), (i, text_offset), 'data', 'data', edgecolor=line_color)
        ax.add_patch(line2)

    # Set proper limits to fit all triangles
    ax.set_xlim(-0.5, len(words) - 0.5)
    ax.set_ylim(-1, len(words) // 2 + 1)

    # Save the image
    plt.savefig(filename, facecolor=bg_color, dpi=300)  # Increase the DPI

    # Show the plot
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')  # For TkAgg, PyGTK
    # manager.frame.Maximize(True)  # For wxPython
    plt.show()

def get_sentence():
    def submit():
        sentence = entry.get()
        bg_color = bg_color_var.get()
        txt_color = txt_color_var.get()
        line_color = line_color_var.get()
        root.destroy()  # Close the window
        if sentence:  # Check if the user input is not empty
            plot_triangles(sentence, bg_color, txt_color, line_color)
        else:
            plot_triangles(bg_color=bg_color, txt_color=txt_color, line_color=line_color)  # Use the default sentence if the user input is empty

    def clear():
        entry.delete(0, 'end')  # Clear the entry field

    root = tk.Tk()
    tk.Label(root, text="Enter a sentence:").pack()

    entry = tk.Entry(root, width=60)  # Increase the width of the entry widget
    entry.insert(0, "a year from now you will wish you started today")  # Prefill the sentence
    entry.pack()

    tk.Button(root, text="Clear", command=clear).pack()  # Add a clear button

    # Color options
    colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple']

    # Label and Dropdown menu for background color
    tk.Label(root, text="Select Background Color").pack()
    bg_color_var = tk.StringVar(root)
    bg_color_var.set('black')  # set default value
    bg_color_option = ttk.Combobox(root, textvariable=bg_color_var, values=colors, width=58)  # Increase the width of the combobox widget
    bg_color_option.pack()

    # Label and Dropdown menu for text color
    tk.Label(root, text="Select Text Color").pack()
    txt_color_var = tk.StringVar(root)
    txt_color_var.set('white')  # set default value
    txt_color_option = ttk.Combobox(root, textvariable=txt_color_var, values=colors, width=58)  # Increase the width of the combobox widget
    txt_color_option.pack()

    # Label and Dropdown menu for line color
    tk.Label(root, text="Select Line Color").pack()
    line_color_var = tk.StringVar(root)
    line_color_var.set('white')  # set default value
    line_color_option = ttk.Combobox(root, textvariable=line_color_var, values=colors, width=58)  # Increase the width of the combobox widget
    line_color_option.pack()

    tk.Button(root, text="Submit", command=submit).pack()
    root.mainloop()

get_sentence()
