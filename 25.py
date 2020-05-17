import requests

response = requests.get("https://api.github.com/users/avielb/repos")
print(response.status_code)
if response.status_code == 200:

    my_repos = response.json()
    my_object = [{"name": "aviel"}, {"name": "david"}, {"name": "moshe"}]
    for repo in my_repos:
        print(repo["full_name"])
