import csv
from os.path import dirname, join
import matplotlib.pyplot as plt
from datetime import datetime
from get_temp_dates import get_tmax_tmin_dates

#file_path = dirname(_)
file_name = '/Users/marksanchez/src/DataVisualization/data/sitka_weather_2018_simple.csv'
death_valley_file = '/Users/marksanchez/src/DataVisualization/data/death_valley_2018_simple.csv'
with open(file_name) as f, open(death_valley_file) as d:
    reader = csv.reader(f)
    dv_reader = csv.reader(d)
    header_row = next(reader)
    dv_header_row = next(dv_reader)
    rainfall = []
    highs = []
    dates = []
    lows = []
    h_l_d = []
    dv_highs = []
    dv_dates = []
    dv_lows = []
    dv_h_l_d = []
    
    h_l_d = get_tmax_tmin_dates(dv_reader, dv_header_row)
    dv_h_l_d = get_tmax_tmin_dates(dv_reader, dv_header_row)
    
    dv_highs = dv_h_l_d[0]
    dv_lows = dv_h_l_d[1]
    dv_dates = dv_h_l_d[2]
    highs = h_l_d[0]
    lows = h_l_d[1]
    #dates = [item[0] for item in h_l_d[2]]
    # print(h_l_d[0])
    # print(h_l_d[1])
    print(len(h_l_d[0]))
    print(len(highs))
    print(len(h_l_d[1]))
    print(len(lows))
    print(len(dv_dates))
    print(h_l_d[2][2])
 
    # plt.style.use('seaborn')
    # fig, ax = plt.subplots()
    # ax.plot(dates, highs, c="blue")
    # #ax.plot(dates, dv_highs, c='red')
    # # ax.plot(dates, lows, c='blue')
    # #shade between two plots
    # plt.fill_between(dates, dv_highs, highs, facecolor='blue')
    # plt.title("Daily high temps", fontsize=24)
    # plt.xlabel("", fontsize=16)
    # fig.autofmt_xdate()
    # plt.ylabel("temp (F)", fontsize=16)
    # plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.show()

