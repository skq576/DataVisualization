import requests
import json

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
# headers = {""}
r = requests.get(url)
response = r.json()
file_path = '/Users/Mark/source/pyworkspace/DataVisualization/data/hn.json'
with open(file_path, 'w') as f:
    json.dump(response, f, indent=4)
    print(len(response))
    for item in response:
        url_new = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
        # print(url_new)
        r1 = requests.get(url_new)
        response1 = r1.json()
        print(response1['title'])


        