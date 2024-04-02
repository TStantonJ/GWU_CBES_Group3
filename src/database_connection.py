import pymongo
from pymongo import MongoClient
import datetime


class DatabaseManager:
    def __init__(self, mongo_host, mongo_port):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port

    def connect_mongo(self, database_name, collection_name):
        """Connect to the database and collection, if the collection does not exist, 
            it will create one."""
        self.database_name = database_name
        self.collection_name = collection_name
        uri = f"mongodb://{self.mongo_host}:{self.mongo_port}/"
        client = MongoClient(uri)
        db = client[self.database_name]
        self.collection = db[self.collection_name]
        return self.collection
    
    def insert(self, data):
        """Insert data to the collection, data should be a list of dictionaries 
            even if it contains only one dictionary."""
        if len(data) > 1:
            self.collection.insert_many(data)
        else:
            self.collection.insert_one(data[0])

    # primitive method to find documents in the collection
    def _find(self, query):
        """Find documents in the collection, if query is not provided, it will return all documents.
        It returns a cursor object. You need to iterate over the cursor to get the documents."""
        return self.collection.find(query)
    
    def find(self, d=None, limit=-1, selected_field=[], sort_by=None):
        """Find documents in the collection, if query is not provided, it will return all documents.
        It returns a list of dictionaries."""
        projection = {}
        projection['_id'] = 0
        if selected_field:
            for field in selected_field:
                projection[field] = 1
        if d:
            cursor = self.collection.find(d, projection)
        else:
            cursor = self.collection.find({}, projection)
        if sort_by:
            cursor = cursor.sort(sort_by,-1)
        if limit > 0:
            cursor = cursor.limit(limit)
        return list(cursor)
          
    def _count(self, query):
        """Count the number of documents in the collection, if query is not provided, 
           it will return the total number of documents in the collection."""
        return self.collection.count_documents(query)
    
    def count(self, field='', value=''):
        if field and value:
            query = {field: value}
        else:
            query = {}
        return self.collection.count_documents(query)
    
    def remove(self, field=None, value=None):
        """Remove a document from the collection, if field is not provided, 
            it will remove all documents."""
        if field and value:
            query = {field: value}
        else:
            query = {}
        self.collection.delete_many(query)

    def _remove(self, query={}):
        """Remove documents from the collection, if query is not provided, 
           it will remove all documents"""
        self.collection.delete_many(query)
        
    def _update_target_field(self, query, new_query):
        """Update the target field in the document"""
        self.collection.update_one(query, {"$set": new_query})

    def _update_all_field(self, query, new_query):
        """Update the target document"""
        self.collection.update(query, new_query)


    def search_bar(self, keyword, language=None, license=None, num = 10, category=None):
        """Search for a document in the collection, return a list of documents that match the search.
            keyword: the name of the project, optional, if not provided, it will return all documents
            language: the language of the project, optional.
            license: the license of the project, optional.
            num: the number of documents to return, optional, default is 10
            category: the field to sort by, users can choose from 
                'stars', 'forks', 'watchers', 'open_issues', 'created_at', 
                'updated_at', 'pushed_at', etc. optional"""
        query = {}
        if language:
            query['language'] = language
        if license:
            query['project_license'] = license
        if keyword:
            query['name'] = keyword
        return self.find(query, limit = num, sort_by = category)
        
def insertion_test():
    data=[{'project_id': 10000, 
           'name': 'xkcd2347', 'full_name': 'tom1', 'owner_id': 33829, 
           'owner_name': 'edsu', 'dependency_project_id': ['Baughn/python-diskcache', 'pytest-dev/pytest', 'theskumar/python-dotenv', 'yaml/pyyaml', 'psf/requests'], 
           'releases': [], 'description': 'Get dependencies for a project on GitHub.', 
           'project_license': 'MIT License', 'html_url': 'https://github.com/edsu/xkcd2347', 
           'language': 'Python', 'default_branch': 'master', 'master_branch': None, 
           'open_issues': 2, 'forks': 1, 'stars': 1200, 'watchers': 13, 'created_at': '2020-08-21T01:47:47Z', 
           'updated_at': '2024-01-18T09:05:33Z', 'pushed_at': '2021-06-17T17:32:26Z', 
           'created_at': '2020-08T17:32:26Z', 'disabled': False},
           {'project_id': 20000, 
           'name': 'xkcd2347', 'full_name': 'jack2', 'owner_id': 33829, 
           'owner_name': 'edsu', 'dependency_project_id': ['Baughn/python-diskcache', 'pytest-dev/pytest', 'theskumar/python-dotenv', 'yaml/pyyaml', 'psf/requests'], 
           'releases': [], 'description': 'Get dependencies for a project on GitHub.', 
           'project_license': 'MIT License', 'html_url': 'https://github.com/edsu/xkcd2347', 
           'language': 'Python', 'default_branch': 'master', 'master_branch': None, 
           'open_issues': 2, 'forks': 1, 'stars': 1000, 'watchers': 13, 'created_at': '2020-08-21T01:47:47Z', 
           'updated_at': '2024-01-18T09:05:33Z', 'pushed_at': '2021-06-17T17:32:26Z', 
           'created_at': '2020-08T17:32:26Z', 'disabled': False},
           {'project_id': 30000, 
           'name': 'xkcd2347', 'full_name': 'lily3', 'owner_id': 33829, 
           'owner_name': 'edsu', 'dependency_project_id': ['Baughn/python-diskcache', 'pytest-dev/pytest', 'theskumar/python-dotenv', 'yaml/pyyaml', 'psf/requests'], 
           'releases': [], 'description': 'Get dependencies for a project on GitHub.', 
           'project_license': 'MIT License', 'html_url': 'https://github.com/edsu/xkcd2347', 
           'language': 'Python', 'default_branch': 'master', 'master_branch': None, 
           'open_issues': 2, 'forks': 1, 'stars': 1500, 'watchers': 13, 'created_at': '2020-08-21T01:47:47Z', 
           'updated_at': '2024-01-18T09:05:33Z', 'pushed_at': '2021-06-17T17:32:26Z', 
           'created_at': '2020-08T17:32:26Z', 'disabled': False}
           ]
    db=DatabaseManager('3.139.100.241', 27017)
    db.connect_mongo("just_for_test", "just_for_test")
    db.insert(data)


def search_test():

    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")

    print(connection.search_bar(keyword='numpy', num = 10, category='stars'))
    

if __name__ == "__main__":
    search_test()
    
