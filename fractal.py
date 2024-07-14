import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

# Define possible shapes
shapes = ['circle', 'square', 'triangle']

# Function to plot a shape at a specified center with a specified color
def plot_shape(ax, center, radius, color, shape):
    if shape == 'circle':
        plot_circle(ax, center, radius, color)
    elif shape == 'square':
        plot_square(ax, center, radius, color)
    elif shape == 'triangle':
        plot_triangle(ax, center, radius, color)

# Function to plot a circle with diameter 1
def plot_circle(ax, center, radius, color):
    circle = plt.Circle(center, 0.5, fill=False, color=color)  # radius is half the diameter
    ax.add_artist(circle)

# Function to plot a square with side length 1
def plot_square(ax, center, radius, color):
    square = plt.Rectangle((center[0] - 0.5, center[1] - 0.5), 1, 1, fill=False, color=color)
    ax.add_artist(square)

# Function to plot a triangle with side length 1
def plot_triangle(ax, center, radius, color):
    height = np.sqrt(3) / 2
    triangle = plt.Polygon([
        (center[0], center[1] + height / 3),
        (center[0] - 0.5, center[1] - height / 3),
        (center[0] + 0.5, center[1] - height / 3),
    ], fill=False, color=color)
    ax.add_artist(triangle)

# Function to calculate the distance from the origin
def distance_from_origin(center):
    return np.sqrt(center[0]**2 + center[1]**2)

# Function to generate a unique color for each circle
def generate_unique_color(index):
    random.seed(index)
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Function to plot shapes with specified color based on distance from the origin
def plot_flower_of_life_and_count_shapes(ax, radius, levels):
    centers = {(0, 0): 0}  # Dictionary to keep track of circle centers and their levels
    shape_counts = {level: {shape: 0 for shape in shapes} for level in range(levels + 1)}

    for level in range(1, levels + 1):
        new_centers = {}
        for center, _ in centers.items():
            # Calculate new centers around each existing center
            for angle in np.linspace(0, 2 * np.pi, num=6, endpoint=False):
                new_center = (round(center[0] + radius * np.cos(angle), 8), round(center[1] + radius * np.sin(angle), 8))
                if new_center not in centers and new_center not in new_centers:
                    new_centers[new_center] = level
                    color = generate_unique_color(len(new_centers) + level * 6)
                    shape = random.choice(shapes)
                    plot_shape(ax, new_center, radius, color, shape)
                    shape_counts[level][shape] += 1
        centers.update(new_centers)
    
    return shape_counts

# Set up the plot for extended layers
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

# Plot the central circle
plot_circle(ax, (0, 0), 1, color='blue')

# Plot the surrounding shapes with colors based on their distance for 93 layers and count them
shape_counts = plot_flower_of_life_and_count_shapes(ax, 1, 93)

# Show gridlines
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()

# Display the shape counts in a table
shape_counts_df = pd.DataFrame(shape_counts).fillna(0).astype(int)
import ace_tools as tools; tools.display_dataframe_to_user(name="Shape Counts with Defined Lengths", dataframe=shape_counts_df.T)
shape_counts_df.T
