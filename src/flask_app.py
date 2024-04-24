import json
import uuid

from flask import Flask, jsonify, request, make_response, send_file

from database_connection import DatabaseManager
from src.json_encoder import JSONEncoder

app = Flask(__name__)


@app.route('/search')
def search_repository():
    keyword = request.args.get('keyword')
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")
    result = connection.search_bar(keyword)[0]

    return jsonify(json.loads(json.dumps(result, cls=JSONEncoder)))


@app.route('/get_repository')
def get_repository():
    full_name = request.args.get('full_name')
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")
    query = {"full_name": full_name}
    result = list(connection._find(query).limit(1))
    if not result:
        return make_response(jsonify({"error": "Content not found"}), 404)

    return jsonify(json.loads(json.dumps(result, cls=JSONEncoder)))


def get_dependency_by_level(full_name, connection):
    initial_query = {"full_name": full_name}
    result = connection._find(initial_query).limit(1)
    if not result:
        return None
    root = result[0]

    q = [root]
    while q:
        # Collect dependencies of all nodes in the current layer
        temp = set()
        for item in q:
            if 'dependency_project_id' in item:
                for dependency in item['dependency_project_id']:
                    temp.add(dependency['full_name'])

        # Query all dependencies
        dependencies_query = {"full_name": {"$in": list(temp)}}
        dependencies_results = list(connection._find(dependencies_query))
        dependencies_dict = {item['full_name']: item for item in dependencies_results}

        # Prepare nodes for the next layer
        next_level = []
        for item in q:
            item['apiCalled'] = True
            if 'dependency_project_id' in item:
                item['children'] = [
                    {**dependencies_dict[dependency['full_name']], 'uuid': str(uuid.uuid4()), 'version': dependency['version']}
                    for dependency in item['dependency_project_id']
                    if dependency['full_name'] in dependencies_dict
                ]
                next_level.extend(item['children'])

        q = next_level

    return root


@app.route('/get_all_dependency')
def get_all_dependency():
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")

    full_name = request.args.get('full_name')

    result = get_dependency_by_level(full_name, connection)

    if result:
        return jsonify(json.loads(json.dumps(result, cls=JSONEncoder)))
    else:
        return make_response(jsonify({"error": "Content not found"}), 404)


@app.route('/get_dependency')
def get_dependency():
    full_name = request.args.get('full_name')
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")
    query = {"full_name": full_name}
    result = list(connection._find(query).limit(1))
    if not result:
        return make_response(jsonify({"error": "Content not found"}), 404)

    result = result[0]

    # modify the json to fit Echarts
    children = []
    for dependency in result['dependency_project_id']:
        child = {
            "name": dependency['full_name'].split('/')[-1],
            "full_name": dependency['full_name'],
            "language": dependency.get('language', None),
            "version": dependency['version'],
            "uuid": str(uuid.uuid4()),
            "children": []
        }
        children.append(child)
    result['children'] = children
    result['apiCalled'] = True

    return jsonify(json.loads(json.dumps(result, cls=JSONEncoder)))


@app.after_request
def after_request_func(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


if __name__ == '__main__':
    app.run(port=8000)
