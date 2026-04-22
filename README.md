# Notes REST API (Flask)

Simple REST API for managing notes built with Python and Flask.

## Features

- Get all notes
- Create a note
- Update a note
- Delete a note
- RESTful endpoints
- JSON responses

## Tech Stack

- Python
- Flask
- REST API

## Endpoints

GET /notes  
POST /notes  
PUT /notes/{id}  
DELETE /notes/{id}

## Example Request

POST /notes

```json
{
  "title": "First note",
  "content": "Hello world"
}
