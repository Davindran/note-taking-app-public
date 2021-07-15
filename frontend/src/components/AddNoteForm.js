import React, {Component} from 'react';

class AddNoteForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      content: '',
      tag: '',
      tagsToAdd: []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.addTag = this.addTag.bind(this);
    this.removeTag = this.removeTag.bind(this);
    this.clearFields = this.clearFields.bind(this);
  }

  handleChange(event) {
    let nam = event.target.name;
    let val = event.target.value;
    this.setState({[nam]: val});
  }

  handleSubmit(event) {
    // creates a note in backend with content and tagsToAdd
    const requestBody = {
      content: this.state.content,
      tags: this.state.tagsToAdd
    
    }
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody)
    };

    fetch('http://localhost:5000/v1/note', requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // repopulate page with all notes, including added note
        this.props.fetchNotes();
      });
    
    // clear fields
    this.setState({
      content: '',
      tag: '',
      tagsToAdd: []
    });

    event.preventDefault();
  }

  addTag(event) {
    let array = [...this.state.tagsToAdd]
    if (!array.includes(this.state.tag) && !(this.state.tag === '')) {
      array.push(this.state.tag);
    }
    this.setState({
      tagsToAdd: array,
      tag: ''
    });

    event.preventDefault();
  }

  removeTag(event, tag) {
    // remove tag from array by ID
    let array = [...this.state.tagsToAdd]
    let index = array.indexOf(tag)
    if (index > -1) {
      array.splice(index, 1);
      this.setState({tagsToAdd: array});
    }

    event.preventDefault();
  }

  clearFields(event) {
    // set all states to empty and resets fields
    this.setState({
      content: '',
      tag: '',
      tagsToAdd: []
    });

    event.preventDefault();
  }

  render () {
    return (
      <div className="col-sm-6">
        <form onSubmit={this.handleSubmit}>
          <fieldset>
              <legend>Add a new note</legend>
              <div className="row">
                  <div className="col-sm-2">
                    <label>Content:</label>
                  </div>
                  <textarea name='content' value={this.state.content} onChange={this.handleChange} />
              </div>
              <div className="row">
                  <div className="col-sm-2">
                    <label>Tags:</label>
                  </div>
                  <div className="input-group">
                    <input name="tag" type="text" value={this.state.tag} onChange={this.handleChange} />
                    <button className="small tertiary" onClick={this.addTag}>Add Tag</button>
                  </div>
              </div>
              <div className="row">
                  <div className="col-md-offset-2">
                    {this.state.tagsToAdd.map((tag) => (
                        <mark className="tag" key={tag}> {tag} <a href="/" onClick={(e) => this.removeTag(e,tag)}>
                          <mark>x</mark>
                        </a></mark> 
                    ))}
                  </div>
              </div>

              <div className="row">
                  <div className="col-md-offset-2">
                      <button className="tertiary">Add Note</button>
                      <button className="secondary" onClick={this.clearFields}>Cancel</button>
                  </div>
              </div>
          </fieldset>
        </form>
      </div>
    )
  }
}

export default AddNoteForm