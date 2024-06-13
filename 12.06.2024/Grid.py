import matplotlib.pyplot as plt

# dataset
x =[1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

#create the plot
plt.plot (x,y1, linestyle = '-', color = 'yellow', linewidth = 3, marker = 'o', markersize = 10, markerfacecolor = 'orange' )
plt.plot (x,y2, linestyle = '--', color = 'green', linewidth = 3, marker = 'x', markersize = 10, markerfacecolor = 'red' )

# title and labels
plt.title("customized line plot with grid")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# create a legent methord with chart  that we have created
plt.legend()

#add the value as grid
plt.grid(True)

#custamize the grid
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)

#display the plot
plt.show()