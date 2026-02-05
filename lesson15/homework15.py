import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# 1. Basic Plotting
# -------------------------------
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x² - 4x + 4")
plt.grid(True)
plt.show()


# -------------------------------
# 2. Sine and Cosine Plot
# -------------------------------
x = np.linspace(0, 2*np.pi, 400)

plt.figure()
plt.plot(x, np.sin(x), linestyle='--', marker='o', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='-', marker='s', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------
# 3. Subplots (2x2)
# -------------------------------
x = np.linspace(-2, 2, 400)
x_log = np.linspace(0, 2, 400)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, x**3)
axs[0, 0].set_title("f(x) = x³")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")

axs[0, 1].plot(x, np.sin(x))
axs[0, 1].set_title("f(x) = sin(x)")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("y")

axs[1, 0].plot(x, np.exp(x))
axs[1, 0].set_title("f(x) = eˣ")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")

axs[1, 1].plot(x_log, np.log(x_log + 1))
axs[1, 1].set_title("f(x) = log(x + 1)")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("y")

plt.tight_layout()
plt.show()


# -------------------------------
# 4. Scatter Plot
# -------------------------------
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Scatter Plot")
plt.grid(True)
plt.show()


# -------------------------------
# 5. Histogram
# -------------------------------
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution")
plt.show()


# -------------------------------
# 6. 3D Surface Plot
# -------------------------------
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, Z)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Surface Plot of cos(x² + y²)")
fig.colorbar(surface)
plt.show()


# -------------------------------
# 7. Bar Chart
# -------------------------------
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()


# -------------------------------
# 8. Stacked Bar Chart
# -------------------------------
labels = ['T1', 'T2', 'T3', 'T4']
category_a = [20, 35, 30, 35]
category_b = [25, 30, 35, 20]
category_c = [15, 20, 25, 30]

x = np.arange(len(labels))

plt.figure()
plt.bar(x, category_a, label='Category A')
plt.bar(x, category_b, bottom=category_a, label='Category B')
plt.bar(
    x,
    category_c,
    bottom=np.array(category_a) + np.array(category_b),
    label='Category C'
)

plt.xlabel("Time Period")
plt.ylabel("Value")
plt.title("Stacked Bar Chart")
plt.xticks(x, labels)
plt.legend()
plt.show()
