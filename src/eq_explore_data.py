import json
from os.path import dirname
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

# file_path = dirname(__file__)
# print(file_path)
filename = '/Users/marksanchez/src/DataVisualization/data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

coordinates = []

# lons, lats = ([],) * 2
lons, lats, mags, hover_texts = [], [], [], []


for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    title = eq_dict['properties']['title']
    hover_texts.append(title)
print(mags[:10])
print(coordinates[:10])

for eq_dict in all_eq_dicts:
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    lons.append(longitude)
    lats.append(latitude)
    coordinates.append({'longitude': longitude, 'latitude': latitude})
print(lons[:5])
print(lats[:5])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

readable_file = '/Users/marksanchez/src/DataVisualization/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

