// src/App.js

import React, {Component} from 'react';
import AddNoteForm from './components/AddNoteForm';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      notes: []
    };
    this.fetchNotes = this.fetchNotes.bind(this);
    this.deleteNote = this.deleteNote.bind(this);
    this.filterNotesByTag = this.filterNotesByTag.bind(this);
  }

  fetchNotes() {
    fetch('http://localhost:5000/v1/note')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      this.setState({notes: data});
    });
  }
  deleteNote(event, id, note) {
    // call endpoint to delete note with id
    const endpoint = 'http://localhost:5000/v1/note/' + id;
    const requestOptions = {
      method: 'DELETE'
    };
    
    fetch(endpoint, requestOptions)
      .then(() => {
        // delete note in state
        let array = [...this.state.notes]
        let index = array.indexOf(note)
        if (index > -1) {
          array.splice(index, 1);
          this.setState({notes: array});
        }
      });
    
    event.preventDefault();
    }
    

  filterNotesByTag(event, tag) {
    // call endpoint to get all notes with given tag
    const endpoint = 'http://localhost:5000/v1/note/tag/' + tag;
    const requestOptions = {
      method: 'GET',
    }

    fetch(endpoint, requestOptions)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      this.setState({notes: data});
    })

    event.preventDefault();
  }
  
  componentDidMount() {
    this.fetchNotes();
  }

  render () {
    return (
      // JSX to render goes here...
      <div className="container">
        <div className="row">
          <AddNoteForm fetchNotes = {this.fetchNotes}/>
          <div className="col-sm-6">
          {this.state.notes.map((note) => (
            <div className="card fluid" key={note.id}>
              <div className="section">{note.content}</div>
              <div className="section">
                {note.tags.map((tag) => (
                  <a href="/" onClick={(e) => this.filterNotesByTag(e, tag)} key={tag}>
                    <mark className="tag">{tag}</mark>
                  </a> 
                ))}
              </div>
              <div className="row">
                  <button className="secondary" onClick={(e) => this.deleteNote(e,note.id, note)}>Delete</button>
              </div>
            </div>
          ))}
          </div>
        </div>
      </div>
    );
  }
}

export default App;