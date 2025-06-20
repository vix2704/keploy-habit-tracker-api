from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models import Habit
from backend.crud import create_habit, get_all_habits, update_habit, delete_habit

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vix2704.github.io"],  # ✅ ONLY THIS
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/habits/")
def create_habit_endpoint(habit: Habit):
    habit_id = create_habit(habit)
    return {"id": habit_id}

@app.get("/habits/")
def read_all_habits():
    return get_all_habits()

@app.put("/habits/{habit_id}")
def update_habit_endpoint(habit_id: str, habit: Habit):
    updated_count = update_habit(habit_id, habit)
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit updated successfully"}

@app.delete("/habits/{habit_id}")
def delete_habit_endpoint(habit_id: str):
    deleted_count = delete_habit(habit_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted successfully"}
