import requests
from plotly.graph_objs import Bar
from plotly import offline
from os.path import dirname, join
import json

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']
names, stars, labels, links = [], [], [], []
for repo_dict in repo_dicts:
    # print(repo_dict['owner']['login'])
    name = repo_dict['name']
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
    url = repo_dict['html_url']
    links.append(f"<a href='{url}'>{name}</a>")
    

data =[{
    'type': 'bar',
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker':{
        'color':'rgb(60, 100, 150)',
        'line':{'width':1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout={
    'title': 'Most-starred Python projects on Github',
    'xaxis': {'title': "Repository"},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

print(len(names))
print(len(stars))
# with open('/Users/Mark/source/pyworkspace/DataVisualization/data/github.json', 'w') as f:
#     json.dump(response_dict, f, indent=4)


