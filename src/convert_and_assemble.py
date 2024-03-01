from src.query_github_api import GitHub_Api

"""
    Put all the info into an object for storage
"""
def convert_api_response(repo_info, releases_info, dependency_info):
    # convert release info
    releases = []
    for release in releases_info:
        temp = {
            "tag_name": release['tag_name'],
            "name": release['name'],
            "html_url": release['html_url']
        }
        releases.append(temp)

    # convert dependency info
    dependencies = []
    for dependency in dependency_info:
        dependencies.append(dependency['repository']['nameWithOwner'])

    # convert repo info
    data = {
        "project_id": repo_info['id'],
        "name": repo_info['name'],
        "full_name": repo_info['full_name'],
        "owner_id": repo_info['owner']['id'],
        "owner_name": repo_info['owner']['login'],
        "dependency_project_id": dependencies,
        "releases": releases,
        "description": repo_info['description'],
        "project_license": repo_info['license']['name'],
        "html_url": repo_info['html_url'],
        "language": repo_info['language'],
        "default_branch": repo_info['default_branch'],
        "master_branch": repo_info.get('master_branch', None),  # master_branch may not exist
        "open_issues": repo_info['open_issues_count'],
        "forks": repo_info['forks_count'],
        "stars": repo_info['stargazers_count'],
        "watchers": repo_info['watchers_count'],
        "created_at": repo_info['created_at'],
        "updated_at": repo_info['updated_at'],
        "pushed_at": repo_info['pushed_at'],
        "disabled": repo_info['disabled']
    }

    return data


"""
    Get all info of a repo and assemble 
    
    Parameters:
    - full_name (str): The full name of the repo. It should look like 'owner/repo_name'
"""
def assemble_api_response(full_name):
    client = GitHub_Api(key="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")
    repo_info = client.search_repositories(full_name)  # TODO: change to another better API
    if repo_info['total_count'] == 0:
        print(f"Cannot find repo: {full_name}")
        return None
    repo_info = repo_info['items'][0]
    releases_info = client.get_releases(full_name)
    dependency_info = client.get_dependencies(repo_info['owner']['login'], repo_info['name'], 1)

    data = convert_api_response(repo_info, releases_info, dependency_info)

    return data


if __name__ == "__main__":
    assemble_api_response('edsu/xkcd2347')
