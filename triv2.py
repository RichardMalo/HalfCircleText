import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk
from tkinter import colorchooser

# Function to choose a color
def choose_color(initial_color):
    color_code = colorchooser.askcolor(initial_color)
    return color_code[1]  # return hex color code

# Function to update GUI colors and plot
def update_colors():
    bg_color = choose_color(root['background'])
    line_color = choose_color('black')
    text_color = choose_color('black')

    # Call the plot function with the chosen colors
    plot_triangles('a year from now you will wish you started today', bg_color, line_color, text_color)

# Function to plot triangles
def plot_triangles(sentence, bg_color, line_color, text_color, filename='outputv1.png'):
    words = sentence.split()
    fig, ax = plt.subplots()

    # set figure background color
    fig.patch.set_facecolor(bg_color)

    # hide axes and ticks
    ax.axis('off')

    # Set the vertical offset for the center of the triangles and the text
    text_offset = 0.1

    for i, word in enumerate(words):
        # Place text with chosen text color
        ax.text(i, -text_offset, word, ha='center', va='center', color=text_color)

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
    plt.savefig(filename)
    plt.show()

# Create GUI
root = tk.Tk()

# Add a button to choose colors
button = tk.Button(root, text="Choose Colors", command=update_colors)
button.pack()

# Start the GUI
root.mainloop()
