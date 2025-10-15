This project is a simple FastAPI application that returns my personal details and a random cat fact from an external API.
The endpoint /me responds with structured JSON data including:
- My name, email, and track
- A timestamp showing when the request was made
- A fun cat fact fetched dynamically from catfact.ninja

Technologies Used were:
- Python 3.11+
- FastAPI
- Uvicorn
- Requests

Installation and Setup
- Create a virtual environment
python -m venv venv
- Activate the environment
venv\Scripts\activate
- Install independencies
pip install -r requirements.txt
- Run the app
uvicorn main:app --reload



Note:
-This task was built as part of the HNG Backend Internship (Stage 1).
-It demonstrates how to integrate FastAPI with an external API using requests, and how to return a clean JSON response.


HNG Backend Task 1 – My FastAPI /me Endpoint

Name: Anita Olang
Email: anitaolang005@gmail.com
Track: Backend (Python / FastAPI)
