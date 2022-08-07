import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make a call to GITHUB API and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    
#header, to specify which version of GitHub API to use
headers = {'Accept': 'application/vnd.github.v4+json'}
    
#make the call to the API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process Results
response_dict = r.json()
repo_dicts = response_dict['items']

#store the names and stars of all repos
repo_names, repo_stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repo_stars.append(repo_dict['stargazers_count'])

#make visualization
data = [{
    'type':'bar',
    'x':repo_names,
    'y':repo_stars,
}]

#layout for the graph
my_layout = {
    'title': 'Most Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title':'Stars'},
}

#plot the graph
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='python_repos.html')
