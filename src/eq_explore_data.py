import json
from os.path import dirname
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

# file_path = dirname(__file__)
# print(file_path)
filename = '/Users/marksanchez/src/DataVisualization/data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

coordinates = []
mags = []
# lons, lats = ([],) * 2
lons = []
lats = []
for eq_dict in all_eq_dicts:
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    lons.append(longitude)
    lats.append(latitude)
    coordinates.append({'longitude': longitude, 'latitude': latitude})
print(lons[:5])
print(lats[:5])

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
print(mags[:10])
print(coordinates[:10])

readable_file = '/Users/marksanchez/src/DataVisualization/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

