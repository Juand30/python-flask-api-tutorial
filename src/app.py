from flask import Flask, jsonify, request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    json_data = json.loads(request_body)
    json_data [{"label": "My third task", "done": False}]
    response_body = json.dumps(json_data)

    return jsonify(response_body)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)