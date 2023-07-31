import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_triangles(sentence, filename='outputv1.png'):
    words = sentence.split()
    fig, ax = plt.subplots()

    # hide axes and ticks
    ax.axis('off')

    # Set the vertical offset for the center of the triangles and the text
    text_offset = 0.1

    for i, word in enumerate(words):
        # Place text
        ax.text(i, -text_offset, word, ha='center', va='center')

    # Create triangles from the first word to every other word
    for i in range(1, len(words)):
        line1 = patches.ConnectionPatch((0, text_offset), (i/2, i/2 + text_offset), 'data', 'data', edgecolor='black')
        ax.add_patch(line1)
        line2 = patches.ConnectionPatch((i/2, i/2 + text_offset), (i, text_offset), 'data', 'data', edgecolor='black')
        ax.add_patch(line2)

    # Set proper limits to fit all triangles
    ax.set_xlim(-0.5, len(words) - 0.5)
    ax.set_ylim(-1, len(words) // 2 + 1)

    # Save the image
    plt.savefig(filename)
    plt.show()

plot_triangles('a year from now you will wish you started today')

