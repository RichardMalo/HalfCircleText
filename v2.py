import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def plot_arcs(sentence, filename='output.png'):
    words = sentence.split()
    fig, ax = plt.subplots()

    # hide axes and ticks
    ax.axis('off')

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal')

    # Set the facecolor of the figure
    fig.patch.set_facecolor('black')

    # Set the vertical offset for the center of the arcs and the text
    text_offset = 0.3  # Adjust this value as needed
    arc_offset = 0.5  # Adjust this value as needed

    spacing_factor = 1.5  # Adjust this value as needed

    for i, word in enumerate(words):
        if i != len(words) - 1:
            # Place text for all words but the last
            ax.text(i * spacing_factor, -text_offset, word, ha='center', va='center', color='white')

        # Create arcs from first word to every other word, but not to the last word
        if 0 < i < len(words) - 1:
            center = ((i * spacing_factor / 2), arc_offset)  # center of circle
            radius = i * spacing_factor / 2  # radius of circle
            arc = patches.Arc(center, 2*radius, 2*radius, theta1=0.0, theta2=180.0, edgecolor='white')
            ax.add_patch(arc)

    # For the last word, place it below all other words
    last_word_position = ((len(words) - 2) * spacing_factor / 2, -len(words)/4 - text_offset)  # Adjust this value as needed
    ax.text(last_word_position[0], last_word_position[1], words[-1], ha='center', va='center', color='white')

    # Set proper limits to fit all arcs
    ax.set_xlim(-0.5, (len(words) - 0.5) * spacing_factor)
    ylim_top = max(arc_offset + len(words) * spacing_factor / 2, len(words) // 2 + arc_offset)
    ylim_bottom = min(-len(words)/2, last_word_position[1] - text_offset)
    ax.set_ylim(ylim_bottom - 0.5, ylim_top + 0.5)  # Adjust this value as needed

    # Save the image
    plt.savefig(filename, facecolor=fig.get_facecolor())
    plt.show()

plot_arcs('a year from now you will wish you started today')
