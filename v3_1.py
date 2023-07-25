import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

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
for i in range(n):
    ax.text(x[i], y[i], words[i], color='white', ha='center')

# Draw arcs from word 1 to every other word, raised slightly above the words
for i in range(1, n-1):  # Exclude the last word
    radius = abs(x[i] - x[0]) / 2
    arc = Arc((radius, 0.5), 2*radius, 2*radius,  # raise the arcs by 0.5
              theta1=0, theta2=180, edgecolor='white', lw=2)
    ax.add_patch(arc)

# Add additional arc that looks like 75% circle for the last word, starting below the first word
radius = abs(x[-1] - x[0]) / 2
arc = Arc((radius, -0.25), 2*radius, 2*radius,  # lower the center of the arc by 0.5
          theta1=180, theta2=360, edgecolor='white', lw=2)
ax.add_patch(arc)

# Remove axes
ax.axis('off')

# Set limits for the plot to accommodate the arcs and words
ax.set_xlim(-1, 2*n+1)
ax.set_ylim(-radius-1, 2*n+1)  # accommodate the change in the center of the last arc

# Save the plot as a JPG file
plt.savefig("outputx1.jpg", facecolor=fig.get_facecolor(), edgecolor='none')

# Show the plot
plt.show()