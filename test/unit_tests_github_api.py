import unittest
from unittest.mock import patch, MagicMock
from src.query_github_api import GitHub_Api


class TestGitHubClient(unittest.TestCase):
    """
        Test the query function with get
    """
    @patch('query_github_api.requests.get')
    def test_query_get_success(self, mock_get):
        client = GitHub_Api(key="key")
        expected_response = {
            'total_count': 1,
            'items': [{'id': 123, 'name': 'TestItem'}]
        }
        mock_get.return_value = MagicMock(status_code=200, json=lambda: expected_response)

        response = client.query('GET', 'https://api.example.com/data', headers={})

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertGreater(json_response['total_count'], 0)
        self.assertTrue(len(json_response['items']) > 0)
        mock_get.assert_called_once_with('https://api.example.com/data', headers={})

    """
        Test the query function with post
    """
    @patch('query_github_api.requests.post')
    def test_query_post_success(self, mock_post):
        client = GitHub_Api(key="key")
        expected_response = {
            'success': True,
            'data': {'id': 123, 'name': 'TestPostItem'}
        }
        mock_post.return_value = MagicMock(status_code=200, json=lambda: expected_response)

        response = client.query('POST', 'https://api.example.com/data', headers={}, q={'query': 'test'})

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response['data'], {'id': 123, 'name': 'TestPostItem'})

        mock_post.assert_called_once_with(
            'https://api.example.com/data',
            headers={},
            json={'query': {'query': 'test'}}
        )

    """
        Simulate POST request returns an error for the first time and needs to be retried.
    """
    @patch('query_github_api.requests.post')
    def test_query_post_with_errors_and_retry(self, mock_post):
        mock_post.side_effect = [
            MagicMock(status_code=200, json=lambda: {"errors": [{"message": "timeout"}]}),
            MagicMock(status_code=200, json=lambda: {"data": "retried data"})
        ]

        client = GitHub_Api(key="key")
        response = client.query('POST', 'https://api.example.com', headers={}, q={})

        # Verify return data after retry
        self.assertEqual(response.json(), {"data": "retried data"})
        self.assertEqual(mock_post.call_count, 2)


if __name__ == '__main__':
    unittest.main()
