This project is a simple yet elegant FastAPI backend application built as part of the HNG Backend Stage 1 Task. The application exposes a single endpoint, /me, which returns structured information about the developer (name, email, and stack), the current UTC timestamp, and a randomly fetched cat fact from an external API. In the event that the external API is unavailable or times out, the application gracefully falls back to a default cat fact message.

The main goal of this task is to demonstrate knowledge of API creation, asynchronous requests, environment configuration, and deployment on a live platform such as Railway.

Overview
The application is built with FastAPI, a modern and high-performance web framework for building APIs with Python.
When a client sends a GET request to the /me endpoint, the app performs the following steps:
- It retrieves basic user information from environment variables — specifically the developer’s email, name, and stack.
- It makes an asynchronous call to CatFact API using the httpx client to fetch a random cat fact.
- It compiles the data into a JSON response containing:
  - The status of the operation
  - User information
  - The current UTC timestamp
  - A cat fact (or a fallback message if the external API fails)
This small service demonstrates practical API design principles: asynchronous I/O, error handling, environment configuration, and JSON response formatting.

Setting Up the Project Locally
To run this project on your local machine, ensure that you have Python 3.9 or later installed. The steps below explain everything you need from cloning the repository to viewing the running app in your browser.
Step 1: Clone the Repository
Begin by cloning this GitHub repository and navigating into the project directory:
git clone https://github.com/nitlang01/hng-backend-task1.git
cd hng-backend-task1

Step 2: Create a Virtual Environment
- Creating a virtual environment isolates your dependencies and avoids version conflicts:
python -m venv venv
- Then activate it:
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

Step 3: Install Dependencies
- Install the required libraries using pip:
pip install -r requirements.txt
If you do not yet have a requirements.txt file, you can create one containing:
- fastapi
- uvicorn
- httpx

Step 4: Add Environment Variables
The application depends on a few environment variables to personalize the /me response.
- Create a file named .env in the root directory and include:
USER_EMAIL=anitaolang005@gmail.com
USER_NAME=Anita Olang
USER_STACK=Python/FastAPI
CATFACT_TIMEOUT=5
FALLBACK_FACT=No cat facts available right now. Try again later.

Each variable provides a specific piece of information:
- USER_EMAIL, USER_NAME, and USER_STACK define your personal details.
- CATFACT_TIMEOUT determines how long the app waits for a response from the CatFact API before falling back.
- FALLBACK_FACT is the default message shown when the API call fails.
You can adjust these values to match your own configuration.

Step 5: Run the Application
Once everything is set up, run the development server with Uvicorn:
uvicorn main:app --reload
By default, the app runs on http://127.0.0.1:8000
.
Open your browser and visit http://127.0.0.1:8000/me
 to see your JSON response.

API /me Endpoint Explanation
This endpoint responds to a GET request with a structured JSON object. Below is an example of what you should see:

{
  "status": "success",
  "user": {
    "email": "anitaolang005@gmail.com",
    "name": "Anita Olang",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T08:54:17.384323+00:00",
  "fact": "When your cat rubs up against you, she is actually marking you as hers with her scent."
}

The fact field changes with each request since it pulls a random cat fact from the CatFact API.
If the API is unreachable, it falls back to the default message defined in FALLBACK_FACT.

How It Works
- Environment Configuration
The app reads all user-specific data from environment variables using Python’s os.getenv(). This makes it easy to customize or deploy the app across different environments without altering the code.
- Asynchronous Request Handling
Using the httpx.AsyncClient, the app fetches a random cat fact asynchronously. This ensures that the application remains efficient even under multiple concurrent requests.
- Error Handling and Fallback
In the event of network failure or timeout, the app catches the exception and substitutes the response with a fallback fact, ensuring that users always receive a valid response.
- Response Construction
The app compiles the final JSON response containing the operation status, user information, timestamp (in UTC), and the cat fact.

Deployment on Railway
Railway provides a simple way to deploy backend projects like this one. Follow these steps to deploy your own version:
- Push your project to GitHub.
- Visit https://railway.app and log in.
- Click “New Project” → “Deploy from GitHub Repo” and select your repository.
Once deployed, go to the Environment Variables section and add the same variables from your .env file (USER_EMAIL, USER_NAME, USER_STACK, etc.).

Railway automatically detects and runs your FastAPI app on port 8080. When the deployment completes, your live app will be available at a domain similar to:
https://hng-backend-task1-production.up.railway.app/me


If you encounter a “502 Bad Gateway” or “Application failed to respond” error, verify the logs and ensure that your app listens on port 8080 (as Railway requires).

Here are some troubleshooting tips
- App returns default details (“Your Name”, etc.):
Check that your environment variables are correctly defined and visible in Railway’s dashboard.
- Deployment succeeded but URL doesn’t respond:
Ensure your FastAPI app runs with uvicorn main:app --host 0.0.0.0 --port 8080 in the Procfile or Railway Start Command section.





Name: Anita Olang
Email: anitaolang005@gmail.com
Stack: Python/FastAPI
