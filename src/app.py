from flask import Flask, jsonify
from flask import request
import json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    # return "<h1>Hello!</h1>"
    json_text = jsonify(todos)
    return json_text
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[0]
    return todos


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

