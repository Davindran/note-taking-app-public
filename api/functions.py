import os
import sqlite3
import requests

def get_database_connection():
    '''
        Creates a connection between selected database
    '''
    sqlite_file = 'notes.db'
    file_exists = os.path.isfile(sqlite_file)
    conn = sqlite3.connect(sqlite_file)
    if not file_exists:
        create_sqlite_tables(conn)
    return conn

def create_sqlite_tables(conn):
    '''
        Creates a sqlite table as specified in schema_sqlite.sql file
    '''
    cursor = conn.cursor()
    with open('schema_sqlite.sql', 'r') as schema_file:
        cursor.executescript(schema_file.read())
    conn.commit()

def create_note(content):
    '''
        Function for adding note into the database
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        # add content of notes into notes table
        cursor.execute("INSERT INTO notes(content) VALUES (?)", (content,))
        conn.commit()
        cursor.close()
        return cursor.lastrowid
    except Exception as e:
        print(e)
        cursor.close()

def add_tag(tag, note_id):
    '''
        Function for adding tag into the database with associated note id
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tags(tag, note_id) VALUES (?, ?)", (tag, note_id))
        conn.commit()
        cursor.close()
        return
    except:
        cursor.close()

def get_all_notes():
    '''
        Function for getting all notes
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM notes')
        results = cursor.fetchall()
        cursor.close()
        return results
    except:
        cursor.close()


def get_all_tags():
    '''
        Function for getting all tags
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT(tag) FROM tags')
        sql_result = cursor.fetchall()
        if len(sql_result) > 0:
            results = []
            for i in sql_result:
                results.append(i[0])
        else:
            results = None
        cursor.close()
        return results
    except:
        cursor.close()

def get_all_tags_for_note(note_id):
    '''
        Get all tags associated with note
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT tag FROM tags WHERE note_id=?', (str(note_id), ))
        results = cursor.fetchall()
        cursor.close()
        return results
    except:
        cursor.close()

def delete_all_entries():
    '''
        Delete all entries in notes and tags tables, reset id sequence
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes")
        cursor.execute("DELETE FROM tags")
        cursor.execute("DELETE FROM sqlite_sequence")
        conn.commit()
        cursor.close()
        return
    except:
        cursor.close()

def get_all_notes_for_tag(tag):
    '''
        Get all notes associated with tag
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM notes WHERE id IN (SELECT note_id FROM tags WHERE tag=?)', (tag, ))
        results = cursor.fetchall()
        cursor.close()
        return results
    except:
        cursor.close()

def append_tags_to_notes(sql_notes):
    '''
        Append tags to each note by given ID
    '''
    results = []
    for i in sql_notes: # parse sql result
        entry = {}
        id = i[0]
        content = i[1]
        tags = []
        sql_tags = get_all_tags_for_note(id)
        for j in sql_tags: # parse sql result
            tags.append(j[0])
        entry['id'] = id
        entry['content'] = content
        entry['tags'] = tags
        results.append(entry)
    return results

def get_one_note(id):
    '''
        Get one note by given ID
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM notes WHERE id=' + str(id))
        results = cursor.fetchall()
        cursor.close()
        return results
    except:
        cursor.close()

def delete_one_note(id):
    '''
        Delete one note by given ID
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id=" + str(id))
        cursor.execute("DELETE FROM tags WHERE note_id=" + str(id))
        conn.commit()
        cursor.close()
        return
    except:
        cursor.close()

def update_note(id, content):
    '''
        Function for updating existing note in database
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        # add content of notes into notes table
        cursor.execute("UPDATE notes SET content=? WHERE id=?", (content,id))
        conn.commit()
        cursor.close()
        return
    except Exception as e:
        print(e)
        cursor.close()

def delete_tags_for_note(note_id):
    '''
        Delete tags for a note with given ID
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tags WHERE note_id=" + str(note_id))
        conn.commit()
        cursor.close()
        return
    except Exception as e:
        print(e)
        cursor.close()

def get_first_last_name():
    '''
        Generates First and Last names from Random User Generator API
    '''
    url = 'https://randomuser.me/api/'
    r = requests.get(url)
    response = r.json()
    first_name = response['results'][0]['name']['first']
    last_name = response['results'][0]['name']['last']
    return first_name, last_name

def get_funny_note(first_name,last_name):
    '''
        Generates a joke from The Internet Chuck Norris Database using provided first and last names
    '''
    url = 'http://api.icndb.com/jokes/random?firstName=' + first_name + '&lastName=' + last_name
    r = requests.get(url)
    response = r.json()
    funny_note = response['value']['joke']
    return funny_note
