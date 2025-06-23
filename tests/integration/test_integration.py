from backend.crud import create_habit, get_all_habits
from backend.models import Habit

def test_create_and_read_habit_integration():
    test_habit = Habit(id="test123", name="Water Plants", description="Every morning", is_complete=False)
    create_habit(test_habit)
    habits = get_all_habits()

    found = False
    for h in habits:
        if h["name"] == "Water Plants":
            found = True
            break
    assert found
