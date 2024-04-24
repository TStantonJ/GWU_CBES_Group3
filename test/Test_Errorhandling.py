import unittest
from unittest.mock import patch, MagicMock
from src.query_github_api import GitHub_Api


class TestGitHubApi(unittest.TestCase):
    @patch('query_github_api.requests.get')
    def test_search_repository_success(self, mock_requests):
        api = GitHub_Api(key='dummy_key')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'name': 'test_repo'}
        mock_requests.return_value = mock_response

        result = api.search_repositories('test_owner/test_repo')

        self.assertEqual(result, {'name': 'test_repo'})

    @patch('query_github_api.requests.get')
    def test_search_repository_failure(self, mock_requests):
        api = GitHub_Api(key='dummy_key')
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests.return_value = mock_response

        with self.assertRaises(RuntimeError):
            api.search_repositories('test_owner/test_repo')

    @patch('query_github_api.requests.post')
    def test_get_dependencies_success(self, mock_requests):
        api = GitHub_Api(key='dummy_key')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': {'repository': {'dependencyGraphManifests': {'nodes': []}}}}
        mock_requests.return_value = mock_response

        result = list(api.get_dependencies('test_owner', 'test_repo'))

        self.assertEqual(result, [])

    @patch('query_github_api.requests.post')
    def test_get_dependencies_failure(self, mock_requests):
        api = GitHub_Api(key='dummy_key')
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = mock_requests.exceptions.HTTPError("500 Server Error")
        mock_requests.return_value = mock_response

        with self.assertRaises(Exception):
            list(api.get_dependencies('test_owner', 'test_repo'))


if __name__ == '__main__':
    unittest.main()
