import matplotlib.pyplot as plt

# dataset
x = [1, 2, 3, 4, 5]
y = [2, 3, 6, 5, 7]

#create a plot with the marker
plt.plot(x, y, marker='o', linestyle='-.', color='g', markersize=10, markerfacecolor='r')

#add the labels as well as the title
plt.title("line plot with markers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# display the plot
plt.show()