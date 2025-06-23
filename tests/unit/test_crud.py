from unittest.mock import MagicMock, patch
from backend.models import Habit
from backend.crud import create_habit, get_all_habits, delete_habit


# Mock habit input
mock_habit = Habit(id="test123", name="Test Habit", description="Testing...", is_complete=False)


@patch("backend.crud.collection.insert_one")
def test_create_habit(mock_insert_one):
    mock_insert_one.return_value.inserted_id = "mocked_id"
    habit_id = create_habit(mock_habit)
    assert habit_id == "mocked_id"
    mock_insert_one.assert_called_once()


@patch("backend.crud.collection.find")
def test_get_all_habits(mock_find):
    mock_find.return_value = [{"_id": "1", "name": "Test", "description": "Desc", "is_complete": False}]
    habits = get_all_habits()
    assert isinstance(habits, list)
    assert habits[0]["name"] == "Test"
    mock_find.assert_called_once()


@patch("backend.crud.collection.delete_one")
def test_delete_habit(mock_delete_one):
    mock_delete_one.return_value.deleted_count = 1
    result = delete_habit("507f1f77bcf86cd799439011")  # 24-char hex string
    assert result == 1
    mock_delete_one.assert_called_once()

from unittest.mock import MagicMock, patch
from backend.models import Habit
from backend.crud import create_habit, get_all_habits, delete_habit


# Mock habit input
mock_habit = Habit(id="test123", name="Test Habit", description="Testing...", is_complete=False)


@patch("backend.crud.collection.insert_one")
def test_create_habit(mock_insert_one):
    mock_insert_one.return_value.inserted_id = "mocked_id"
    habit_id = create_habit(mock_habit)
    assert habit_id == "mocked_id"
    mock_insert_one.assert_called_once()


@patch("backend.crud.collection.find")
def test_get_all_habits(mock_find):
    mock_find.return_value = [{"_id": "1", "name": "Test", "description": "Desc", "is_complete": False}]
    habits = get_all_habits()
    assert isinstance(habits, list)
    assert habits[0]["name"] == "Test"
    mock_find.assert_called_once()


@patch("backend.crud.collection.delete_one")
def test_delete_habit(mock_delete_one):
    mock_delete_one.return_value.deleted_count = 1
    result = delete_habit("507f1f77bcf86cd799439011")  # 24-char hex string
    assert result == 1
    mock_delete_one.assert_called_once()

