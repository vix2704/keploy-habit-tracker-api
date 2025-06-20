from .database import collection
from bson.objectid import ObjectId

def create_habit(habit):
    result = collection.insert_one(habit.dict())
    return str(result.inserted_id)

def get_all_habits():
    habits = []
    for habit in collection.find():
        habit["_id"] = str(habit["_id"])
        habits.append(habit)
    return habits

def update_habit(habit_id, habit_data):
    result = collection.update_one(
        {"_id": ObjectId(habit_id)},
        {"$set": habit_data.dict(exclude_unset=True)}
    )
    return result.modified_count

def delete_habit(habit_id):
    result = collection.delete_one({"_id": ObjectId(habit_id)})
    return result.deleted_count
