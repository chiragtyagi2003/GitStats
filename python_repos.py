import requests

#Make a call to GITHUB API and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    
#header, to specify which version of GitHub API to use
headers = {'Accept': 'application/vnd.github.v4+json'}
    
#make the call to the API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#store the API response in a variable
response_dict = r.json()

print(f"Total Repositories: {response_dict['total_count']}")

#info about repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#selected info about the each repo
print("\nInformation About Each Repository:")
print("\n")
for repo_dict in repo_dicts:
    
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print("\n")