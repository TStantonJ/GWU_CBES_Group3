'''
Show the repository list by enter the username.

Prompts the user by entering the GitHub username,
fetches the list of repositories for this user using the GitHub API,
then get the print of the name of repositories.
The output variable contains the string file sent as a response by the GitHub.
'''

import requests
import json

User = input("Enter the Username to print the repository list: ")
url = "https://api.github.com/users/{}/repos".format(User)

data = {"type": "all", "sort": "full_name", "direction": "asc"}

output = requests.get(url, data = json.dumps(data))
output = json.loads(output.text)

for i in output:
    print(i["name"])