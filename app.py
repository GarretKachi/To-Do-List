#!/usr/bin/python3
'''
   Flash file for the To-do-list app
'''
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "text": "Complete assignment", "completed": False},
    {"id": 2, "text": "Read a book", "completed": True}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "text": request.json.get('text'),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['text'] = request.json.get('text', task['text'])
            task['completed'] = request.json.get('completed', task['completed'])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
