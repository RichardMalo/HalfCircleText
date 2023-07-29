import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# Sentence to print and split into words
sentence = "a year from now you will wish you started today"
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

# Print words on the plot with white color
for i in range(n):  # Include the last word now
    ax.text(x[i], y[i], words[i], color='white', ha='center')

# Draw triangles from word 1 to every other word, with increasing size
for i in range(1, n):
    triangle = Polygon([(x[i-1], y[i-1]), (x[i-1] + (x[i]-x[i-1])/2, y[i-1] + i), (x[i], y[i])], 
                       closed=False, fill=None, edgecolor='white')
    ax.add_patch(triangle)

# Remove axes
ax.axis('off')

# Set limits for the plot to accommodate the triangles and words
ax.set_xlim(-1, 2*n+1)
ax.set_ylim(-2, max(y) + n + 1)  # accommodate the triangles' height

# Save the plot as a JPG file
plt.savefig("output_triangles.jpg", facecolor=fig.get_facecolor(), edgecolor='none')

# Show the plot
plt.show()
