import unittest
from src.convert_and_assemble import convert_api_response

class TestConvertApiResponse(unittest.TestCase):

    def test_convert_api_response(self):
        repo_info = {
            'id': '123',
            'name': 'TestRepo',
            'full_name': 'User/TestRepo',
            'owner': {'id': '456', 'login': 'TestUser'},
            'description': 'This is a test repository',
            'license': {'name': 'MIT'},
            'html_url': 'https://github.com/User/TestRepo',
            'language': 'Python',
            'default_branch': 'main',
            'master_branch': 'main',
            'open_issues_count': 10,
            'forks_count': 5,
            'stargazers_count': 20,
            'watchers_count': 25,
            'created_at': '2020-01-01T00:00:00Z',
            'updated_at': '2021-01-01T00:00:00Z',
            'pushed_at': '2022-01-01T00:00:00Z',
            'disabled': False
        }

        releases_info = [
            {'tag_name': 'v1.0', 'name': 'Version 1.0', 'html_url': 'https://github.com/User/TestRepo/releases/v1.0'}
        ]

        dependency_info = [
            {'repository': {'nameWithOwner': 'User/DependencyRepo1'}},
            {'repository': {'nameWithOwner': 'User/DependencyRepo2'}}
        ]

        result = convert_api_response(repo_info, releases_info, dependency_info)

        self.assertEqual(result['project_id'], '123')
        self.assertEqual(result['name'], 'TestRepo')
        self.assertEqual(result['full_name'], 'User/TestRepo')
        self.assertEqual(result['owner_id'], '456')
        self.assertEqual(result['owner_name'], 'TestUser')
        self.assertEqual(result['description'], 'This is a test repository')
        self.assertEqual(result['project_license'], 'MIT')
        self.assertEqual(result['html_url'], 'https://github.com/User/TestRepo')
        self.assertEqual(result['language'], 'Python')
        self.assertEqual(result['default_branch'], 'main')
        self.assertEqual(result['open_issues'], 10)
        self.assertEqual(result['forks'], 5)
        self.assertEqual(result['stars'], 20)
        self.assertEqual(result['watchers'], 25)
        self.assertEqual(result['created_at'], '2020-01-01T00:00:00Z')
        self.assertEqual(result['updated_at'], '2021-01-01T00:00:00Z')
        self.assertEqual(result['pushed_at'], '2022-01-01T00:00:00Z')
        self.assertEqual(result['disabled'], False)

        self.assertEqual(result['dependency_project_id'], ['User/DependencyRepo1', 'User/DependencyRepo2'])

        self.assertEqual(len(result['releases']), 1)
        self.assertEqual(result['releases'][0]['tag_name'], 'v1.0')
        self.assertEqual(result['releases'][0]['name'], 'Version 1.0')
        self.assertEqual(result['releases'][0]['html_url'], 'https://github.com/User/TestRepo/releases/v1.0')


if __name__ == '__main__':
    unittest.main()
