import requests
import json

#Задание_1
url = 'https://api.github.com'
user='ekaterinaredko'
req = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(req.json(), f)
for i in req.json():
    print(i['name'])
#Geekbrains_Libraries
#Geekbrains_Python
#Geekbrains_SQL

#Задание_2
url = 'https://api.github.com/user'
user='ekaterinaredko'
token = 'secret'
req = requests.get(url, auth=(user, token))
print(req.json())
#{'login': 'ekaterinaredko', 'id': 78317661, 'node_id': 'MDQ6VXNlcjc4MzE3NjYx', 'avatar_url': 'https://avatars.githubusercontent.com/u/78317661?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/ekaterinaredko', 'html_url': 'https://github.com/ekaterinaredko', 'followers_url': 'https://api.github.com/users/ekaterinaredko/followers', 'following_url': 'https://api.github.com/users/ekaterinaredko/following{/other_user}', 'gists_url': 'https://api.github.com/users/ekaterinaredko/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/ekaterinaredko/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/ekaterinaredko/subscriptions', 'organizations_url': 'https://api.github.com/users/ekaterinaredko/orgs', 'repos_url': 'https://api.github.com/users/ekaterinaredko/repos', 'events_url': 'https://api.github.com/users/ekaterinaredko/events{/privacy}', 'received_events_url': 'https://api.github.com/users/ekaterinaredko/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': None, 'twitter_username': None, 'public_repos': 3, 'public_gists': 0, 'followers': 0, 'following': 0, 'created_at': '2021-01-31T18:14:05Z', 'updated_at': '2021-10-06T18:38:18Z', 'private_gists': 0, 'total_private_repos': 1, 'owned_private_repos': 1, 'disk_usage': 122, 'collaborators': 0, 'two_factor_authentication': False, 'plan': {'name': 'free', 'space': 976562499, 'collaborators': 0, 'private_repos': 10000}}
