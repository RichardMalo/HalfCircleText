import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

def create_sentence_plot(sentence="a year from now you will wish you started today"):
    # Sentence to print and split into words
    words = sentence.split(' ')

    # Create a figure and axes with black background
    fig, ax = plt.subplots(figsize=(10, 10))  # make the figure larger
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Set aspect ratio so that circles look like circles
    ax.set_aspect('equal')

    # Number of words and index for positioning
    n = len(words)

    # Calculate the x and y coordinates for words with increased spacing
    x = np.linspace(0, 2*n, n)
    y = [0] * n

    # Define the radius for the arcs connecting words
    radius = abs(x[-2] - x[0]) / 2

    # Print words on the plot with white color
    for i in range(n-1):  # Exclude the last word for now
        ax.text(x[i], y[i], words[i], color='white', ha='center')

    # Add the last word under the start of the bottom white arc
    ax.text(radius, -radius - 1, words[-1], color='white', ha='center')

    # Draw arcs from word 1 to every other word, raised slightly above the words
    for i in range(1, n-1):  # Exclude the last word
        radius_i = abs(x[i] - x[0]) / 2
        arc = Arc((radius_i, 0.5), 2*radius_i, 2*radius_i,  # raise the arcs by 0.5
                  theta1=0, theta2=180, edgecolor='white', lw=2)
        ax.add_patch(arc)

    # Define the start and end points of the arcs
    start_arc_1, end_arc_1 = 180, 270
    start_arc_2, end_arc_2 = 270, 360

    # Create two arcs
    arc_1 = Arc((radius, -0.25), 2*radius, 2*radius, 
                theta1=start_arc_1, theta2=end_arc_1, edgecolor='black', lw=2)
    arc_2 = Arc((radius, -0.25), 2*radius, 2*radius, 
                theta1=start_arc_2, theta2=end_arc_2, edgecolor='white', lw=2)

    # Add the arcs to the plot
    ax.add_patch(arc_1)
    ax.add_patch(arc_2)

    # Remove axes
    ax.axis('off')

    # Set limits for the plot to accommodate the arcs and words
    ax.set_xlim(-1, 2*n+1)
    ax.set_ylim(-radius-2, radius+2)  # accommodate the change in the center of the last arc

    # Save the plot as a JPG file
    plt.savefig("outputv4.png", facecolor=fig.get_facecolor(), edgecolor='none')

    # Show the plot
    plt.show()

def get_sentence():
    def submit():
        sentence = entry.get()
        root.destroy()  # Close the window
        if sentence:  # Check if the user input is not empty
            create_sentence_plot(sentence)
        else:
            create_sentence_plot()  # Use the default sentence if the user input is empty

    root = tk.Tk()
    tk.Label(root, text="Enter a sentence:").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Submit", command=submit).pack()
    root.mainloop()

get_sentence()