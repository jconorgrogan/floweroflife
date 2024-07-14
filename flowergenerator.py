import matplotlib.pyplot as plt
import numpy as np

# Function to plot a circle with a specified color
def plot_circle(ax, center, radius, color):
    circle = plt.Circle(center, radius, fill=False, color=color)
    ax.add_artist(circle)

# Function to calculate the distance from the origin
def distance_from_origin(center):
    return np.sqrt(center[0]**2 + center[1]**2)

# Function to plot circles with specified color based on distance from the origin and count circles
def plot_flower_of_life_and_count_efficient(ax, radius, levels):
    centers = {(0, 0): 0}  # Dictionary to keep track of circle centers and their levels
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow']
    level_counts = {0: 1}  # Initial center at level 0
    color_counts = {color: 0 for color in colors}
    color_counts['blue'] = 1  # Central circle is blue

    for level in range(1, levels + 1):
        new_centers = {}
        for center, _ in centers.items():
            # Calculate new centers around each existing center
            for angle in np.linspace(0, 2 * np.pi, num=6, endpoint=False):
                new_center = (round(center[0] + radius * np.cos(angle), 8), round(center[1] + radius * np.sin(angle), 8))
                if new_center not in centers and new_center not in new_centers:
                    new_centers[new_center] = level
                    distance = distance_from_origin(new_center)
                    color_index = int(distance / radius) % len(colors)
                    color = colors[color_index]
                    plot_circle(ax, new_center, radius, color=color)
                    color_counts[color] += 1
        centers.update(new_centers)
        level_counts[level] = len(new_centers)
    
    return level_counts, color_counts

# Set up the plot for extended layers
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

# Plot the central circle
plot_circle(ax, (0, 0), 1, color='blue')

# Plot the surrounding circles with colors based on their distance and count them for 13 layers
efficient_level_counts, color_counts = plot_flower_of_life_and_count_efficient(ax, 1, 13)

# Show gridlines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()

print("Level counts:", efficient_level_counts)
print("Color counts:", color_counts)
