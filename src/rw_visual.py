from matplotlib import pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(rw.x_values[0],rw.y_values[0], c='red', s=200)
    ax.scatter(rw.x_values[rw.num_points - 1],rw.y_values[rw.num_points - 1], c='red', s=200)
    plt.show()

    keep_running = input("Plot another walk: (y/n)")
    if keep_running == "n":
        break
# elif keep_running != "y":
#     ""