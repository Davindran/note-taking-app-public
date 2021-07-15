# Note Taking App
## Introduction
This note taking app allows you to take down and manage your notes easily. It is powered by a REST service developed with Flask and a UI developed with React.
## Features
### Backend
- Create a note with tags
- Generate a funny random note
- Get all notes
- Delete all notes
- Get one note by ID
- Update one note by ID
- Delete one note by ID
- Get all notes by a specified tag
- Get all tags

For detailed examples of requests and responses, view [README.md](/api/README.md) located in the /api directory.

### Frontend
- Create a note with tags
- View all notes currently in the database
- View notes filtered by tag
- Delete a note

## Getting started
To run this application, you will need [Python 3](https://www.python.org/downloads/) and [Node](https://nodejs.org/en/) installed on your system.

Clone this repository:

`git clone https://github.com/Davindran/note-taking-app.git`

Install the Python Flask dependencies by simply executing in the project directory:

`pip3 install -r requirements.txt`

Change directory into the `api` folder and start the backend Flask application:

`cd api`

`python3 app.py`

Open a new terminal, change directory into the `frontend` folder and start the frontend React application:

`cd frontend`

`yarn start`

Visit `localhost:3000` on your web browser to start using the app. Alternatively, requests can be sent directly to the backend Flask application at `localhost:5000`.

On the left hand, you can use the form to add new notes, including a button `Add Tag` to add tags one by one. The tags are displayed below the input text with the option to be deleted. On the bottom of the form,  `Cancel` will delete all the values in the form, including the tags and `Add Note` will create a new note in the backend.

The right hand side displays a list of all the notes inside the system, including their tags; each tag is clickable and will filter the list of notes by that particular tag (i.e., If I click on the `work` tag it should show me all notes tagged with the `work` tag). The `Delete` button will delete the note.
