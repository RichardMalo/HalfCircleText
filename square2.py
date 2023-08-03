import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_squares(words):
    fig, ax = plt.subplots()

    # plot the words
    for i, word in enumerate(words):
        plt.text(i+1, 0, word, ha='center', va='center')

    # draw squares
    for i in range(1, len(words)):
        # midpoint between first word and current word
        mid_x = (1 + i+1) / 2

        # height and width of the square
        height = i
        width = i

        # coordinates of the vertices of the square (excluding the bottom line)
        vertices = [
            (mid_x - width / 2, 0.5),         # bottom-left vertex
            (mid_x - width / 2, 0.5 + height), # top-left vertex
            (mid_x + width / 2, 0.5 + height), # top-right vertex
            (mid_x + width / 2, 0.5)           # bottom-right vertex
        ]

        # create a path
        square_path = mpath.Path(vertices)

        # draw a square centered above the midpoint of first word and current word
        square = patches.PathPatch(square_path, linewidth=3, edgecolor='r', facecolor='none')
        ax.add_patch(square)

    # adjust the limits of the plot
    plt.xlim(0, len(words)+1)
    plt.ylim(-1, len(words)+1)

    # hide the axis
    plt.axis('off')

    # set the aspect of the plot to be equal, so the square appears as a square
    ax.set_aspect('equal')

    return fig

def plot_squares():
    # get the sentence from the entry
    sentence = entry.get()

    # split the sentence into words
    words = sentence.split()

    # draw squares
    fig = draw_squares(words)

    # create a canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # place the canvas on the window
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=4)

# create a window
root = tk.Tk()

# create an entry
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3)

# create a button
button = tk.Button(root, text='Plot squares', command=plot_squares)
button.grid(row=0, column=3)

root.mainloop()