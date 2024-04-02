import json

from flask import Flask, jsonify, request, make_response, send_file

from database_connection import DatabaseManager
from src.json_encoder import JSONEncoder

app = Flask(__name__)


@app.route('/get_repository')
def get_repository():
    full_name = request.args.get('full_name')
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")
    query = {"full_name": full_name}
    result = list(connection.find(query).limit(1))
    if not result:
        return make_response(jsonify({"error": "Content not found"}), 404)

    return jsonify(json.loads(json.dumps(result, cls=JSONEncoder)))


@app.route('/get_dependency')
def get_dependency():
    full_name = request.args.get('full_name')
    connection = DatabaseManager('3.139.100.241', 27017)
    connection.connect_mongo("test_database", "test_collection")
    query = {"full_name": full_name}
    result = list(connection.find(query).limit(1))
    if not result:
        return make_response(jsonify({"error": "Content not found"}), 404)

    result = result[0]

    # modify the json to fit Echarts
    children = []
    for dependency in result['dependency_project_id']:
        child = {
            "name": dependency.split('/')[-1],
            "full_name": dependency,
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
