from random import choice
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die():
    """Create a 6 sided die"""
    def __init__(self):
        self.previous_rolls = []
    
    def roll_die(self):
        x = choice([1, 2, 3, 4, 5, 6])
        self.previous_rolls.append(x)
        return x

if __name__ == "__main__":
    die_1 = Die()
    die_2 = Die()
    results = []

    # x = die1.roll_die()
    # print(x)

    for roll in range(1000):
        a = die_1.roll_die()
        b = die_2.roll_die()
        result = a + b
        results.append(result)
    #print(die.previous_rolls)

    frequencies = []

    for value in range(1, 13):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)

    #Visualize the results
    x_values = list(range(1, 13))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Result of rolling D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

        

        