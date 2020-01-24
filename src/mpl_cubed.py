import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [num**3 for num in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=100)
plt.show()