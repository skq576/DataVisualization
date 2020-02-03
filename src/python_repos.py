import requests

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# store api response in a variable
response_dict = r.json()
print(f"Total repos: {response_dict['total_count']}")

#Explore info about the repos
repo_dicts = response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")

#examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print(f"name: {repo_dict['name']}")
print(f"Description: {repo_dict['description']}")

#process results
print(response_dict.keys())