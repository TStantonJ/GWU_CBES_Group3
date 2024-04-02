from flask import Flask, request
from bs4 import BeautifulSoup
from flask_cors import CORS
import requests
import json
from datetime import *
import lxml
import ontology
import git_project
import json


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/search-results/<term>")
def searchResults(term):
    print("search term is: " + term)

    lang = request.args.get("lang", default="C")

    if lang == "C++": 
        lang = "C%2B%2B"
    elif lang == "C#":
        lang  = 'C%23'
    else:
        lang = 'C'

    url = f'https://github.com/search?l={lang}&o=desc&s=updated&type=Repositories&q={term}&p=1'

    response = requests.get(url)

    html_content = response.content
    print("response status is : " + str(response.status_code))
    soup = BeautifulSoup(html_content, 'html.parser')

    search_results = soup.find_all('li', {'class':'repo-list-item'})
    count = 1

    results = []

    ##
    ontology.clear_onto()


    for each_result in search_results:
        sample_code = str(each_result)
    
        print(10*'*')
        print(f"Repo details for search result {count}")
        soup2 = BeautifulSoup(sample_code,'html.parser') # repo name
        soup3 = BeautifulSoup(sample_code,'html.parser') # repo language
        soup4 = BeautifulSoup(sample_code,'html.parser') # repo license
        soup5 = BeautifulSoup(sample_code,'html.parser') # 

        repo_name = soup2.find('a',{'class':'v-align-middle'}).get_text().strip()
        
        print(f'''Repo name = {repo_name}''')

        repoDetails = soup3.find_all('div', {'class':'mr-3'})
        number_of_details = len(repoDetails)
        date_rel = "Updated " + each_result.select_one('relative-time').get_text().strip()
    

        ## TODO may just want like 3 retries here if number_of_details comes back empty
        
        print(f"Number of details present in the repo: " + str(number_of_details))

        details = []
        for each_detail in repoDetails:
            cleaned : str = each_detail.text.strip()
            print(cleaned)
            if not cleaned.__contains__('Updated'): # use the properly-formatted datetime from Git's html, not what's being displayed
                details.append(cleaned)

        details.append(date_rel) ## corrected date

        result = {'name': repo_name, 'details' : details}

       

        proj = git_project.GitProject(result['name'], result['details'])
        print("project license is:  " + proj.license)
        

        results.append(proj.__dict__)
        
        newProj = ontology.create_project(proj.name, proj.owner, proj.lang, [proj.license], proj.stars, proj.updated)
        print("new proj was created in ontology, name is : " + newProj.title)
        count = count + 1
    ontology.sync_ontology_updates()
    print("Success")

    ## this is purely test code, logs returned projects
    returnedOntResult1 = ontology.get_individuals_Project_WithLastModified()
    for res in returnedOntResult1:
        print("returned from ontology :" + res) 


    return results

@app.route("/file-structure")
def fileStructure():
    args = request.args
    user = args["user"]
    projName = args["projName"]

    current_location = request.args.get("fullRoute", default= "")
    route = current_location.replace("-", "/")

    print("full route is :  " + current_location)

    print("user is : " + user)
    data = []

    url = f'https://github.com/{user}/{projName}/{route}'

    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    list_of_content = soup.find_all('div',{'role':'row','class':'Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item'})

    
    for content in list_of_content:
        content_name = content.find('div', {'role': 'rowheader'}).get_text().strip()
        content_type_temp = content.svg
        content_url = (content.a)['href']
        content_type = content_type_temp['aria-label']
        today = datetime.now()
        #content_updated_tag = content.find('relative-time')
        content_updated_tag = content.select_one('relative-time')
        if content_updated_tag is not None:
            content_updated = content_updated_tag.text
        else:
            content_updated = "N/A"
        data.append({'content_name': str(content_name), 'content_type': str(content_type), 'content_updated': str(content_updated), 'URL': str(content_url)})



    for d in data:
        print(d)

    return data

@app.route("/dependencies")
def dependencies():
    args = request.args
    user = args["user"]
    projName = args["projName"]

    # Define the URL of the repository page
    url = f'https://github.com/{user}/{projName}/network/dependencies'

    # Send a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Find the README.md file and extract its contents
    dependencies_list = soup.find_all('div', {'data-test-selector':'dg-repo-pkg-dependency'})

    dependencies = []
    if dependencies_list:
        
        for all_dep in dependencies_list:
            #temp = BeautifulSoup(all_dep, 'html.parser')
            dependency_name = all_dep.find('a',{'data-hovercard-type':'dependendency_graph_package'}).get_text().strip()
            dependency_version = all_dep.find('span',{'data-view-component':'true'}).get_text().strip()
            dependencies.append({'dependency_name':f'{dependency_name}','dependency_version':f'{dependency_version}'})
        print(dependencies)

    else:
        print("No dependencies")
    return dependencies

@app.route("/filter-results/")
def filter_results():
    print("Filter functions")
    language = None
    stars = request.args.get("stars", default = None)
    license = request.args.get("license", default = None)
    last_update = request.args.get("date", default = None)
    result = ontology.intersection_of_filters(license,language,last_update,stars)

    # results = []

    # for each_result in result:
    #     temp_repo = getattr(ontology.onto,each_result)
    #     temp_result = {
    #     "project_name": f"{temp_repo.title}",
    #     "project_owner": f"{temp_repo.owner}",
    #     "language": f"{temp_repo.hasLanguage}",
    #     "license": "MIT",
    #     "stars": f"{temp_repo.has_Stars}",
    #     "last_update": f"{temp_repo.has_Date_LastModified}"
    #     }
    #     results.append(temp_result)

    return result

'''
  {
      "project_name": "sample-project-2",
      "project_owner": "user2",
      "language": "C",
      "license": "MIT",
      "stars": 200,
      "last_update": "2023-01-15"
    }
'''