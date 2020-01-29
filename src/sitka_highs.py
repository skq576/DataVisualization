import csv
from os.path import dirname, join
import matplotlib.pyplot as plt
from datetime import datetime

#file_path = dirname(_)
file_name = '/Users/marksanchez/src/DataVisualization/data/death_valley_2018_simple.csv'

with open (file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    header_num = 0
    for header in header_row:
        print(str(header_num) + " " + header)
        header_num = header_num + 1
    highs = []
    dates = []
    lows = []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)
        try:
            high = int(row[4])
            highs.append(high)
        except:
            print(f"invalid high value for {date}")
            high = 0
            highs.append(high)
        try:
            low = int(row[5])
            lows.append(low)
        except:
            print(f"invalid low value for {date}")
            low = 0
            lows.append(low)
    #print(highs)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    #shade between two plots
    plt.fill_between(dates, highs, lows, facecolor='blue')
    plt.title("Daily high temps", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("temp (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


