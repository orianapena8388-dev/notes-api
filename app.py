from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []
next_id = 1


@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)


@app.route('/notes', methods=['POST'])
def create_note():
    global next_id
    data = request.get_json()

    note = {
        "id": next_id,
        "title": data.get("title"),
        "content": data.get("content")
    }

    notes.append(note)
    next_id += 1

    return jsonify(note), 201


@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()

    for note in notes:
        if note["id"] == note_id:
            note["title"] = data.get("title")
            note["content"] = data.get("content")
            return jsonify(note)

    return jsonify({"error": "Note not found"}), 404


@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return jsonify({"message": "Deleted"})

    return jsonify({"error": "Note not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)