import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# 2. Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# 3. Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# 4. Box Plot
plt.boxplot(y)
plt.title("Box Plot")
plt.show()
