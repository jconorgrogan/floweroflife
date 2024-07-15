import matplotlib.pyplot as plt
import numpy as np

# Function to plot a circle
def plot_circle(ax, center, radius, color='b', linestyle='-'):
    circle = plt.Circle(center, radius, edgecolor=color, facecolor='none', linestyle=linestyle)
    ax.add_artist(circle)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.grid(True)

# Circle 1: Unit circle centered at (0, 0)
plot_circle(ax, (0, 0), 1, color='b')

# Circle 2: Circle centered at (1, 0) with radius 1
plot_circle(ax, (1, 0), 1, color='r')

# Draw hexagon around the original unit circle
hexagon_points = [(np.cos(np.pi/3 * i), np.sin(np.pi/3 * i)) for i in range(6)]

# Points for the lines
line_points = [(0, 0), (1, 0)] + hexagon_points[1:5]  # Up to the 5th node of the hexagon

# Final points for the lines
line_points.append(hexagon_points[5])  # 5th node of the hexagon
point7 = (hexagon_points[5][0] + 1, hexagon_points[5][1])  # 1 unit across the x-axis
line_points.append(point7)
point8 = (2, 0)  # New point at (2,0)
line_points.append(point8)
point9 = (1.5, np.sqrt(3)/2)  # Intersection point of the red circle and the new circle
line_points.append(point9)
point10 = (1, 2*np.sqrt(3)/2)  # New point at (1, 2sqrt(3)/2)
line_points.append(point10)
point11 = (0, 2*np.sqrt(3)/2)  # New point at (0, 2sqrt(3)/2)
line_points.append(point11)
point12 = (-1, 2*np.sqrt(3)/2)  # New point at (-1, 2sqrt(3)/2)
line_points.append(point12)
point13 = (-1.5, np.sqrt(3)/2)  # New point at (-1.5, sqrt(3)/2)
line_points.append(point13)
point14 = (-2, 0)  # New point at (-2, 0)
line_points.append(point14)
point15 = (-1.5, -np.sqrt(3)/2)  # New point at (-1.5, -sqrt(3)/2)
line_points.append(point15)
point16 = (-1, -2*np.sqrt(3)/2)  # New point at (-1, -2sqrt(3)/2)
line_points.append(point16)
point17 = (0, -2*np.sqrt(3)/2)  # New point at (0, -2sqrt(3)/2)
line_points.append(point17)
point18 = (1, -2*np.sqrt(3)/2)  # New point at (1, -2sqrt(3)/2)
line_points.append(point18)
point19 = (2, -2*np.sqrt(3)/2)  # New point at (2, -2sqrt(3)/2)
line_points.append(point19)
point20 = (2.5, -np.sqrt(3)/2)  # Corrected point at (2.5, -sqrt(3)/2)
line_points.append(point20)
point21 = (3, 0)  # New point at (3, 0)
line_points.append(point21)

line_x, line_y = zip(*line_points)
ax.plot(line_x, line_y, color='k', label='Tracing Line')

# Label each line segment starting from 1
for i in range(len(line_points) - 1):
    x_values = [line_points[i][0], line_points[i+1][0]]
    y_values = [line_points[i+1][1], line_points[i][1]]
    ax.text((x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2, f'{i+1}', 
            color='blue', fontsize=12, ha='center')

# Draw dotted circles at each vertex of the hexagon
for i, (x, y) in enumerate(hexagon_points):  # Including the last point to close the loop
    plot_circle(ax, (x, y), 1, color=f'C{i}', linestyle=':')

# Draw new circles centered at points 7 to 21 with radius 1
plot_circle(ax, point7, 1, color='g', linestyle='-')
plot_circle(ax, point8, 1, color='m', linestyle='-')
plot_circle(ax, point9, 1, color='c', linestyle='-')
plot_circle(ax, point10, 1, color='y', linestyle='-')
plot_circle(ax, point11, 1, color='orange', linestyle='-')
plot_circle(ax, point12, 1, color='purple', linestyle='-')
plot_circle(ax, point13, 1, color='pink', linestyle='-')
plot_circle(ax, point14, 1, color='brown', linestyle='-')
plot_circle(ax, point15, 1, color='grey', linestyle='-')
plot_circle(ax, point16, 1, color='cyan', linestyle='-')
plot_circle(ax, point17, 1, color='lime', linestyle='-')
plot_circle(ax, point18, 1, color='gold', linestyle='-')
plot_circle(ax, point19, 1, color='navy', linestyle='-')
plot_circle(ax, point20, 1, color='teal', linestyle='-')
plot_circle(ax, point21, 1, color='maroon', linestyle='-')

# Set plot limits and labels
ax.set_xlim(-3, 5)
ax.set_ylim(-4, 4)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a legend
ax.legend()

# Display the plot
plt.show()
