from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" for the to-do list
todos = []

# Routes for CRUD operations on To-Do List
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json.get('task')
    todos.append({'task': new_todo, 'completed': False})
    return jsonify({'message': 'Todo added!'}), 201

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = not todos[index]['completed']
        return jsonify({'message': 'Todo updated!'}), 200
    else:
        return jsonify({'error': 'Invalid index'}), 400


@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    todos.pop(index)
    return jsonify({'message': 'Todo deleted!'})

if __name__ == '__main__':
    app.run(debug=True)

