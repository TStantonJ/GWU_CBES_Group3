# search repositories by name
for repo in g.search_repositories("pythoncode tutorials"):
    # print repository details
    print_repo(repo)

# search by programming language
for i, repo in enumerate(g.search_repositories("language:python")):
    print_repo(repo)
    print("="*100)
    if i == 9:
        break