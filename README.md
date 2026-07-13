# Backend AI Week 1 Assignment

This project is part of the FlyRank AI Backend Engineering Internship.

## Features

- FastAPI backend server
- Two JSON endpoints
- Tested using browser and curl

## Endpoints

### GET /

Returns a welcome message.

Example response:

```json
{
  "message": "Hello from FlyRank Backend AI Internship!"
}
```

### GET /about

Returns basic information.

Example response:

```json
{
  "name": "Sreepathi Gnaneshwar",
  "track": "Backend AI Engineering",
  "week": 1
}
```

## Run Locally

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs