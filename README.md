# Habit Tracker API

A professional, full-stack habit tracking application featuring a FastAPI backend with MongoDB and a polished frontend**.

> Developed as part of the Keploy API Fellowship (June 2025)

---

## Features

* **FastAPI** backend with MongoDB database integration
* Interactive frontend with custom UI and weekly tracking interface
* Ability to **add**, **view**, and **delete** habits
* 7-day circular checkboxes for routine tracking
* Clean separation of frontend and backend

---

## Tech Stack

* **Backend:** FastAPI, Uvicorn, Pydantic, Motor
* **Frontend:** HTML, CSS (custom design), Vanilla JavaScript
* **Database:** MongoDB Atlas (cloud-hosted)
* **Deployment:** Render (backend), GitHub Pages (frontend)

---

## Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/vix2704/keploy-habit-tracker-api.git
cd keploy-habit-tracker-api
```

### 2. Set up virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend/` directory:

```env
MONGODB_URL=mongodb+srv://<your_mongo_uri>
```

### 5. Start the backend server

```bash
cd backend
uvicorn main:app --reload
```

Access the API documentation here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run the frontend

Open `frontend/index.html` in a web browser.

---

## Deployment (Live Demo URLs)

* **Backend:** https\://<your-backend-on-render>
* **Frontend:** [https://vix2704.github.io/keploy-habit-tracker-api/](https://vix2704.github.io/keploy-habit-tracker-api/)

---

## Author

**Vijaya Mahato**
Software development enthusiast focused on full-stack API projects
[LinkedIn](https://linkedin.com/in/vix2704) · [GitHub](https://github.com/vix2704)

---

## License

This project is licensed under the MIT License.
