import matplotlib.pyplot as plt

# dataset
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 7]

# create a plot for our data
plt.plot(x, y)

# customization of the plot

# add a title
plt.title("Line Plot")

# add x and y Labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# output the plot
plt.show()