import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")  # Use this backend for compatibility with tkinter and the window manager.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

def create_sentence_plot(sentence="a year from now you will wish you started today", bg_color='black', txt_color='white', line_color='white', capitalize=False):
    # Sentence to print and split into words
    if capitalize:
        sentence = sentence.title()
    words = sentence.split(' ')

    # Create a figure and axes with selected background
    fig, ax = plt.subplots(figsize=(10, 10))  # make the figure larger
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # Set aspect ratio so that circles look like circles
    ax.set_aspect('equal')

    # Number of words and index for positioning
    n = len(words)

    # Calculate the x and y coordinates for words with increased spacing
    x = np.linspace(0, 2*n, n)
    y = [0] * n

    # Define the radius for the arcs connecting words
    radius = abs(x[-2] - x[0]) / 2

    # Print words on the plot with selected color
    for i in range(n-1):  # Exclude the last word for now
        ax.text(x[i], y[i], words[i], color=txt_color, ha='center')

    # Add the last word under the start of the bottom white arc
    ax.text(radius, -radius - 1, words[-1], color=txt_color, ha='center')

    # Draw arcs from word 1 to every other word, raised slightly above the words
    for i in range(1, n-1):  # Exclude the last word
        radius_i = abs(x[i] - x[0]) / 2
        arc = Arc((radius_i, 0.5), 2*radius_i, 2*radius_i,  # raise the arcs by 0.5
                  theta1=0, theta2=180, edgecolor=line_color, lw=2)
        ax.add_patch(arc)

    # Define the start and end points of the arcs
    start_arc_1, end_arc_1 = 180, 270
    start_arc_2, end_arc_2 = 270, 360

    # Create two arcs
    arc_1 = Arc((radius, -0.25), 2*radius, 2*radius, 
                theta1=start_arc_1, theta2=end_arc_1, edgecolor=bg_color, lw=2)
    arc_2 = Arc((radius, -0.25), 2*radius, 2*radius, 
                theta1=start_arc_2, theta2=end_arc_2, edgecolor=line_color, lw=2)

    # Add the arcs to the plot
    ax.add_patch(arc_1)
    ax.add_patch(arc_2)

    # Remove axes
    ax.axis('off')

    # Set limits for the plot to accommodate the arcs and words
    ax.set_xlim(-1, 2*n+1)
    ax.set_ylim(-radius-2, radius+2)  # accommodate the change in the center of the last arc

    # Save the plot as a JPG file
    plt.savefig("outputv7.png", dpi=600, facecolor=fig.get_facecolor(), edgecolor='none')

    # Show the plot
    manager = plt.get_current_fig_manager()

    # Get the current matplotlib backend
    backend = matplotlib.get_backend()

    if 'TkAgg' in backend:
        manager.window.state('zoomed')
    elif 'wxAgg' in backend:
        manager.frame.Maximize(True)
    elif 'QT4Agg' in backend:
        manager.window.showMaximized()
    else:
        print(f"Warning: The current backend ({backend}) may not support window maximization.")
    
    plt.show()

def get_sentence():
    def submit():
        sentence = entry.get()
        bg_color = bg_color_var.get()
        txt_color = txt_color_var.get()
        line_color = line_color_var.get()
        capitalize = var_capitalize.get()
        root.destroy()  # Close the window
        if sentence:  # Check if the user input is not empty
            create_sentence_plot(sentence, bg_color, txt_color, line_color, capitalize)
        else:
            create_sentence_plot(bg_color=bg_color, txt_color=txt_color, line_color=line_color, capitalize=capitalize)  # Use the default sentence if the user input is empty
    
    def clear():
        entry.delete(0, 'end')  # Clear the entry field

    root = tk.Tk()
    tk.Label(root, text="Enter a sentence:").pack()
    
    entry = tk.Entry(root, width=60)  # Increase the width of the entry widget
    entry.insert(0, "a year from now you will wish you started today")  # Prefill the sentence
    entry.pack()
    
    tk.Button(root, text="Clear", command=clear).pack()  # Add a clear button
    
    # Color options
    colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple', 'aqua', 'magenta', 'lime', 'teal', 'maroon', 'navy', 'olive', 'silver', 'gray', 'pink', 'cyan', 'orange', 'brown']

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

    # Checkbutton for capitalizing every first letter of each word
    var_capitalize = tk.BooleanVar()
    var_capitalize.set(False)  # set default value
    tk.Label(root, text="Capitalize first letter of each word").pack()
    chk_capitalize = tk.Checkbutton(root, variable=var_capitalize)
    chk_capitalize.pack()

    tk.Button(root, text="Submit", command=submit).pack()
    root.mainloop()

get_sentence()