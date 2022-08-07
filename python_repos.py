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

#process the results
#keys of the response dict
print(response_dict.keys())
