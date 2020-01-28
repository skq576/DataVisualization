import csv
from os.path import dirname, join

#file_path = dirname(_)
file_name = '/Users/marksanchez/src/DataVisualization/data/sitka_weather_07-2018_simple.csv'

with open (file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # header_num = 0
    # for header in header_row:
    #     print(str(header_num) + " " + header)
    #     header_num = header_num + 1
    for index, header in enumerate(header_row):
        print(index, header)
