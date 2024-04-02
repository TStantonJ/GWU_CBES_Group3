import logging
from collections import deque

import convert_and_assemble
from database_connection import DatabaseManager
from src.query_github_api import GitHub_Api


def search_and_save(query):
    """
        Search repos via constructed query and save the assembled info into DB

        param query:
            (https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#constructing-a-search-query)
    """
    client = GitHub_Api()
    try:
        search_results = client.search_repositories(query)
    except Exception as e:
        logging.error(f"Failed to search query: {query} due to: {e}")
        return

    if search_results is None:
        logging.error(f"Search result for query: {query} is None.")
        return

    queue = deque(item['full_name'] for item in search_results['items'])  # Only keep their full_name
    seen = set()  # de-duplicate repos

    # DB client
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")  # TODO update DB info

    while queue:
        cur = queue.popleft()
        if cur in seen:
            continue
        seen.add(cur)

        # checking if this repo exists in DB
        query = {"full_name": "cur"}
        result = list(connection.find(query))
        if result is not None and len(result) > 0:
            continue

        try:
            assembled_result = convert_and_assemble.assemble_api_response(cur)
            if assembled_result is None:
                logging.warning(f"No assembled result for {cur}, skipping...")
                continue

            # Insert the assembled_result into DB
            connection.insert([assembled_result])
            logging.info(f"Insert repo info: {cur}")

            # Add the dependencies of the current repo to wait-list
            for dependency in assembled_result['dependency_project_id']:
                if dependency not in seen:  # Prevent re-adding seen dependencies
                    queue.append(dependency)
        except Exception as e:
            logging.error(f"Error processing repo {cur}: {e}")
            continue


if __name__ == "__main__":
    search_and_save('gwu+in:name+language%3AC%2B%2B+language%3AC+&sort=stars&per_page=100&page=1')