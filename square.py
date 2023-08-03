import matplotlib.pyplot as plt
import matplotlib.patches as patches

# position of the words along the x-axis
x_word1 = 1
x_word2 = 2
x_word3 = 3

# arbitrary y-values
y_word1 = 0
y_word2 = 0
y_word3 = 0

fig, ax = plt.subplots()

# plot the words
plt.text(x_word1, y_word1, 'word1', ha='center', va='center')
plt.text(x_word2, y_word2, 'word2', ha='center', va='center')
plt.text(x_word3, y_word3, 'word3', ha='center', va='center')

# midpoint between "word1" and "word2"
mid_x_12 = (x_word1 + x_word2) / 2

# midpoint between "word1" and "word3"
mid_x_13 = (x_word1 + x_word3) / 2

# height and width of the smaller square
height_small = 1
width_small = 1

# height and width of the larger square
height_large = 2
width_large = 2

# draw a square centered above the midpoint of "word1" and "word2"
square1 = patches.Rectangle((mid_x_12 - width_small / 2, y_word1 + 0.5), width_small, height_small, linewidth=3, edgecolor='r', facecolor='none')
ax.add_patch(square1)

# draw a larger square centered above the midpoint of "word1" and "word3"
square2 = patches.Rectangle((mid_x_13 - width_large / 2, y_word1 + 0.5), width_large, height_large, linewidth=3, edgecolor='r', facecolor='none')
ax.add_patch(square2)

# adjust the limits of the plot
plt.xlim(0, 4)
plt.ylim(-1, 3)

# hide the axis
plt.axis('off')

# set the aspect of the plot to be equal, so the square appears as a square
ax.set_aspect('equal')

plt.show()