import matplotlib.pyplot as plt

plt.style.use('dark_background')
squares = [1, 4, 9, 16, 25]
x_values = range(1, 1000)
input_values = [1, 2, 3, 4, 5]
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#set chart title and lable axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
plt.savefig('squares.plot.png', bbox_inches='tight')
