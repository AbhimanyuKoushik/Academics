import numpy as np
import matplotlib.pyplot as plt

# Define x range and function
x = np.linspace(-5, 11.5, 1000)
y = 2 * x**2 - 13 * x + 9

# Points to mark
roots = [(0.7878, 0), (5.7122, 0)]

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$y = 2x^{2} - 13x + 9$', color='red')

# Mark the roots
for root in roots:
    plt.scatter(root[0], root[1], color='blue', label=f'({root[0]:.4f}, {root[1]})')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

# Save and show the plot
plt.savefig("fig.png")
plt.show()

