# Sung Jinwoo AI Chatbot

An AI-powered streaming chatbot inspired by Sung Jinwoo from Solo Leveling.

Live Demo:
[Sung Jinwoo Chatbot](https://sung-jinwoo-chatbot-production.up.railway.app/)

---

## Features

* Real-time AI response streaming
* FastAPI backend
* Clean frontend using HTML, Tailwind CSS, and JavaScript
* GROQ API integration
* OpenAI-compatible client usage
* Railway cloud deployment
* CORS enabled backend
* Responsive chat interface

---

## Tech Stack

### Frontend

* HTML
* Tailwind CSS
* JavaScript

### Backend

* FastAPI
* Pydantic
* StreamingResponse

### AI

* GROQ API
* OpenAI Python Client

### Deployment

* Railway

---

## What I Learned

This project taught me a lot about real-world AI deployment and backend development, including:

* Deploying FastAPI applications on Railway
* Handling ports and environment variables
* Debugging deployment issues
* Serving frontend using FastAPI
* API routing and streaming responses
* CORS handling
* Connecting frontend and backend
* Git and GitHub deployment workflow
* Building a public AI API endpoint

This is my first fully deployed AI chatbot project.

---

## Run Locally

Clone the repository:

```bash
git clone <https://github.com/VirensinIITBHU/sung-jinwoo-chatbot>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python main.py
```

---

## API Endpoint

### POST `/chat`

Request:

```json
{
  "message": "Arise"
}
```

Returns streamed AI response.

---

## Future Improvements

* Better UI/UX
* Chat history
* Authentication
* Memory support
* Voice interaction
* React frontend
* Vector database integration
* RAG pipeline

---

## Author

Virendra Singh
IIT BHU Student | AI & Fullstack Enthusiast
