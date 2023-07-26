import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def plot_arcs(sentence, filename='outputv1.png'):
    words = sentence.split()
    fig, ax = plt.subplots()

    # hide axes and ticks
    ax.axis('off')

    # Set the vertical offset for the center of the arcs and the text
    text_offset = 0.1
    arc_offset = 0.3

    for i, word in enumerate(words):
        # Place text
        ax.text(i, -text_offset, word, ha='center', va='center')

        # Create arcs from first word to every other word, but not to the last word
        if 0 < i < len(words) - 1:
            center = ((i / 2), arc_offset)  # center of circle
            radius = i / 2  # radius of circle
            arc = patches.Arc(center, i, i, theta1=0.0, theta2=180.0, edgecolor='black')
            ax.add_patch(arc)

    # Set proper limits to fit all arcs
    ax.set_xlim(-0.5, len(words) - 0.5)
    ax.set_ylim(-1, len(words) // 2 + 1 + arc_offset)

    # Save the image
    plt.savefig(filename)
    plt.show()

plot_arcs('a year from now you will wish you started today')