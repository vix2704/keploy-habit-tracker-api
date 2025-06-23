# Habit Tracker API

A Full-stack habit tracking application featuring a FastAPI backend with MongoDB and a polished frontend.

|| Developed as part of the Keploy API Fellowship (June 2025)

## Features

A custom API made using FastAPI backend with MongoDB database integration✨ Interactive frontend with custom UI and weekly tracking interface➕ ➖ Ability to add, view, and delete habits🔘 7-day circular checkboxes for routine tracking

## Tech Stack

Backend: FastAPI, Uvicorn, Pydantic, MotorFrontend: HTML, CSS (custom design), Vanilla JavaScriptDatabase: MongoDB Atlas (cloud-hosted)Deployment: Render (backend), GitHub Pages (frontend)

## Getting Started Locally

git clone https://github.com/vix2704/keploy-habit-tracker-api.git
cd keploy-habit-tracker-api

python -m venv venv
venv\Scripts\activate  # For Windows

pip install -r requirements.txt

Create a .env file inside the backend/ directory:

MONGODB_URL=mongodb+srv://<your_mongo_uri>

Start the backend server:

cd backend
uvicorn main:app --reload

Access the API documentation at: http://127.0.0.1:8000/docs

To run the frontend, open frontend/index.html in a web browser.

## Deployment (Live Demo)

Frontend: https://vix2704.github.io/keploy-habit-tracker-api/Backend: https://

## Testing

Wrote unit, integration, and API tests using pytest, pytest-cov, httpx, and mongomock.

To run all tests and measure coverage:

python -m pytest --cov=backend tests/

✅ Total Coverage: 79%✅ Tools Used: pytest, pytest-cov, httpx, unittest.mock, mongomock

📸 Test Coverage Screenshot:
1.API tests
![image](https://github.com/user-attachments/assets/c45b0c6c-f30e-42e1-bee9-307703be89fd)
2.Unit tests
![image](https://github.com/user-attachments/assets/68d67711-a036-41f8-a09b-02b87c153422)
3. Integration tests
![image](https://github.com/user-attachments/assets/e851378f-2efc-46c6-b1b9-f915dae4f499)


Author

Vijaya Mahato Software development enthusiast focused on full-stack API projects 

License

This project is licensed under the MIT License.
