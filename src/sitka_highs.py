import csv
from os.path import dirname, join
import matplotlib.pyplot as plt
from datetime import datetime
from get_temp_dates import get_tmax_tmin_dates

file_name = '/Users/marksanchez/src/DataVisualization/data/sitka_weather_2018_simple.csv'
death_valley_file = '/Users/marksanchez/src/DataVisualization/data/death_valley_2018_simple.csv'
with open(file_name) as f, open(death_valley_file) as d:
    reader = csv.reader(f)
    dv_reader = csv.reader(d)
    header_row = next(reader)
    dv_header_row = next(dv_reader)
    # initialize multiple lists at once
    highs, lows, dates, h_l_d = ([], ) * 4
    dv_highs, dv_lows, dv_dates, dv_h_l_d = ([], ) * 4
    #use module to Get temp and dates from csv no matter header order
    h_l_d = get_tmax_tmin_dates(reader, header_row)
    dv_h_l_d = get_tmax_tmin_dates(dv_reader, dv_header_row)
    
    #mismatch on dates between sitka and DV
    dv_highs = dv_h_l_d[0][:363]
    dv_lows = dv_h_l_d[1]
    dv_dates = dv_h_l_d[2][:363]
    highs = h_l_d[0]
    lows = h_l_d[1]
    dates = h_l_d[2]

 
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="blue")
    ax.plot(dates, dv_highs, c='red')
    #shade between two plots
    plt.fill_between(dates, dv_highs, highs, facecolor='blue')
    plt.title("Daily high temps", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("temp (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

