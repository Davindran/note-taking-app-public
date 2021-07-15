import flask
from flask import request, jsonify
import functions
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/')
def home():
    return '''<h1>Note Taking App</h1>
<p>A REST API for taking notes.</p>'''

@app.errorhandler(404)
def id_not_found(id):
    message = 'Note with ID ' + str(id) + ' not found'
    error_obj = {'message': message, 'id': id}
    return jsonify(error_obj), 404

@app.route('/v1/note', methods=['POST'])
def create_note():
    # parse content, tags from request
    data = request.json
    content = data['content']
    tags = data['tags']
    # add note, tags to db
    note_id = functions.create_note(content)
    for tag in tags:
        functions.add_tag(tag, note_id)
    return get_one_note(note_id)

@app.route('/v1/note', methods=['GET'])
def get_all_notes():
    sql_notes = functions.get_all_notes()
    results = functions.append_tags_to_notes(sql_notes)
    return jsonify(results)

@app.route('/v1/tags', methods=['GET'])
def get_all_tags():
    tags = functions.get_all_tags()
    print(tags)
    return jsonify(tags)

@app.route('/v1/note', methods=['DELETE'])
def delete_all_entries():
    functions.delete_all_entries()
    return '', 204

@app.route('/v1/note/tag/<tag>', methods=['GET'])
def get_all_notes_for_tag(tag):
    sql_notes = functions.get_all_notes_for_tag(tag)
    results = functions.append_tags_to_notes(sql_notes)
    return jsonify(results)

@app.route('/v1/note/<id>', methods=['GET'])
def get_one_note(id):
    sql_note = functions.get_one_note(id)
    if len(sql_note) == 0:
        return id_not_found(id)
    results = functions.append_tags_to_notes(sql_note)
    return jsonify(results)

@app.route('/v1/note/<id>', methods=['DELETE'])
def delete_one_note(id):
    functions.delete_one_note(id)
    return '', 204

@app.route('/v1/note/<id>', methods=['POST'])
def update_note(id):
    # check if note exists
    sql_note = functions.get_one_note(id)
    if len(sql_note) == 0:
        return id_not_found(id)
    # parse content, tags from request
    data = request.json
    content = data['content']
    tags = data['tags']
    # update note
    functions.update_note(id,content)
    # delete old tags
    functions.delete_tags_for_note(id)
    # add new tags
    for tag in tags:
        functions.add_tag(tag, id)
    # display result of addition to db and return as result
    return get_one_note(id)

@app.route('/v1/note/funny', methods=['POST'])
def create_funny_note():
    # get first and last name
    first_name, last_name = functions.get_first_last_name()
    r = functions.get_first_last_name()
    # generate note content from first and last name
    content = functions.get_funny_note(first_name,last_name)
    tag = 'funny'
    # add note, tags to db
    note_id = functions.create_note(content)
    functions.add_tag(tag, note_id)
    return get_one_note(note_id)


app.run()