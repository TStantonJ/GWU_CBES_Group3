import requests
import json

# print the total number of repositories
print(f"Total repositories: {response_dict['total_count']}")

# store list of dictionaries with information about GitHub repositories
repo_dicts = response_dict['items']

# print length of repo_dicts
print(f"Repositories returned: {len(repo_dicts)}")

# select first repository using index
repo_dict = repo_dicts[0]

# print number of keys in individual repository dictionary
print(f"\nKeys: {len(repo_dict)}")

# print all keys in the dictionary using a for loop to iterate over keys in the dictionary
for key in sorted(repo_dict.keys()):
  print(key)

  # select first dictionary for first repository using index
repo_dict = repo_dicts[0]

# print header information before key values return
print("\nSelected information about first repository:")

# print repo name
print(f"Name: {repo_dict['name']}")

# print repository owner information
print(f"Owner: {repo_dict['owner']['login']}")

# print repository number of stars
print(f"Stars: {repo_dict['stargazers_count']}")

# print project URL
print(f"Repository URL: {repo_dict['html_url']}")

# print repository creation date
print(f"Created: {repo_dict['created_at']}")

# print repository last update time
print(f"Updated: {repo_dict['updated_at']}")

# print repository description
print(f"Description: {repo_dict['description']}")