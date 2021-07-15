# Note Taking App
## Backend
This page details example requests sent to the backend Flask application and the expected responses.

## Domain

A Note is composed by three fields:

 * `id`: integer
 * `content`: String
 * `tags`: An array of String

```json
{
  "id": 553363,
  "content": "This is a note",
  "tags": [
    "work",
    "project-1"
  ]
}
```

Example of an error message:

* `id`: integer
* `message`: String

```json
{
  "message": "Note with ID 1 not found",
  "id": 1
}
```

## Endpoint Definitions

### Create a note

Create a basic note

* URL: `/v1/note`
* Method: POST
* Request: A json object with `content` and `tags`
```json
{
  "content": "Don't forget to upload screenshots",
  "tags": [
    "work", "project-1"
  ]
}
```
* Response: 200 Status Code, A full Note 
```json
{
  "id": 553364,
  "content": "Don't forget to upload screenshots",
  "tags": [
    "work",
    "project-1"
  ]
}
```

Example Request:
```bash
curl -X POST "http://127.0.0.1:8000/v1/note" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"content\":\"Don't forget to upload screenshots\",\"tags\":[\"work\",\"project-1\"]}"
```

### Funny Random note

Creates a funny note based on two APIs: the [Random User Generator](https://randomuser.me/) and the [Internet Chuck Norris Database](http://www.icndb.com/api/)

* URL: `/v1/note/funny`
* Method: POST
* Response: 200 Status Code, A note with a Chuck Norris fact, but attributed to a random user, and the tag `funny`
```json
{
  "id": 10,
  "content": "Luukas Niskanen does not code in cycles, he codes in strikes.",
  "tags": [
    "funny"
  ]
}
```

Example Request:
```bash
curl -X POST "http://127.0.0.1:8000/v1/note/funny" -H  "accept: application/json"
```

### Get all the notes

Get all the notes stored in the system

* URL: `/v1/note`
* Method: GET
* Response: 200 Status Code, A list of notes
```json
[
  {
    "id": 5,
    "content": "COMPLETED: My task",
    "tags": [
      "study",
      "completed"
    ]
  },
  {
    "id": 6,
    "content": "It is believed dinosaurs are extinct due to a giant meteor. That's true if you want to call Elena Castro a giant meteor.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 7,
    "content": "Agnes Rodrigues eats lightning and shits out thunder.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 8,
    "content": "When Bruce Banner gets mad, he turns into the Hulk. When the Hulk gets mad, he turns into Olivia Justi.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 9,
    "content": "Sammy Douglas can build a snowman out of rain.",
    "tags": [
      "funny"
    ]
  }
]
```

Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/v1/note" -H  "accept: application/json"
```

### Delete all notes

Delete all the notes in the system

* URL: `/v1/note`
* Method: DELETE
* Response: 204 Status Code, empty body

Example Request:
```bash
curl -X DELETE "http://127.0.0.1:8000/v1/note" -H  "accept: */*"
```

### Get one note

Get a note stored in the system, or an error message if doesn't exist.

* URL: `/v1/note/{id}`
* Method: GET
* Response: 200 Status Code, A single Note
```json
{
  "id": 10,
  "content": "Luukas Niskanen does not code in cycles, he codes in strikes.",
  "tags": [
    "funny"
  ]
} 
```

_or_ 404, error message

```json
{
  "message": "Note with ID 1 not found",
  "id": 1
}
```


Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/v1/note/10" -H  "accept: application/json"
```

### Update a note

Update a note

* URL: `/v1/note/{id}`
* Method: POST
* Request: A json object with `content` and `tags`
```json
{
  "content": "Not funny anymore",
  "tags": [
    "boring"
  ]
}
```
* Response: 200 Status Code, A full Note
```json
{
  "id": 553364,
  "content": "Not funny anymore",
  "tags": [
    "boring"
  ]
}
```

_or_ 404, error message

```json
{
  "message": "Note with ID 1 not found",
  "id": 1
}
```


Example Request:
```bash
curl -X PUT "http://127.0.0.1:8000/v1/note/553364" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"content\":\"Not funny anymore\",\"tags\":[\"boring\"]}"
```

### Delete one note

Delete one note

* URL: `/v1/note/{id}`
* Method: DELETE
* Response: 204 Status Code, empty body

Example Request:
```bash
curl -X DELETE "http://127.0.0.1:8000/v1/note/1" -H  "accept: */*"
```

### Get all the notes for a tag

Get all the notes with the same tag

* URL: `/v1/note/tag/{tag}`
* Method: GET
* Response: 200 Status Code, A list of notes
```json
[
  {
    "id": 6,
    "content": "It is believed dinosaurs are extinct due to a giant meteor. That's true if you want to call Elena Castro a giant meteor.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 7,
    "content": "Agnes Rodrigues eats lightning and shits out thunder.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 8,
    "content": "When Bruce Banner gets mad, he turns into the Hulk. When the Hulk gets mad, he turns into Olivia Justi.",
    "tags": [
      "funny"
    ]
  },
  {
    "id": 9,
    "content": "Sammy Douglas can build a snowman out of rain.",
    "tags": [
      "funny"
    ]
  }
]
```

Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/v1/note/tag/funny" -H  "accept: application/json"
```

### Get all tags

Get all the tags stored in the system

* URL: `/v1/tags`
* Method: GET
* Response: 200 Status Code, A list of tags
```json
[
  "boring",
  "work",
  "study"
]
```

Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/v1/tags" -H  "accept: application/json"
```
