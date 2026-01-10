"""
Unit tests for TodoService.
"""
import pytest
from src.todo_app.domain.entities import Todo
from src.todo_app.application.repositories import InMemoryTodoRepository
from src.todo_app.application.services import TodoService


class TestTodoService:
    """Test cases for the TodoService."""

    def setup_method(self):
        """Set up a fresh repository and service for each test."""
        self.repository = InMemoryTodoRepository()
        self.service = TodoService(self.repository)

    def test_add_todo_creates_new_todo(self):
        """Test that adding a todo creates a new todo with correct properties."""
        title = "New task"

        result = self.service.add_todo(title)

        assert result is not None
        assert result.id is not None
        assert result.title == title
        assert result.completed is False

        # Verify it's in the repository
        saved_todo = self.repository.find_by_id(result.id)
        assert saved_todo is not None
        assert saved_todo.title == title

    def test_add_todo_fails_with_invalid_title(self):
        """Test that adding a todo with invalid title raises ValueError."""
        with pytest.raises(ValueError):
            self.service.add_todo("")

    def test_get_todo_returns_existing_todo(self):
        """Test that getting a todo returns the correct todo."""
        original_todo = Todo.create(title="Test task")
        self.repository.save(original_todo)

        result = self.service.get_todo(original_todo.id)

        assert result is not None
        assert result.id == original_todo.id
        assert result.title == original_todo.title
        assert result.completed == original_todo.completed

    def test_get_todo_returns_none_for_nonexistent_todo(self):
        """Test that getting a non-existent todo returns None."""
        result = self.service.get_todo("nonexistent-id")

        assert result is None

    def test_list_todos_returns_all_todos(self):
        """Test that listing todos returns all saved todos."""
        todo1 = Todo.create(title="Task 1")
        todo2 = Todo.create(title="Task 2")
        self.repository.save(todo1)
        self.repository.save(todo2)

        todos = self.service.list_todos()

        assert len(todos) == 2
        todo_ids = {todo.id for todo in todos}
        assert todo1.id in todo_ids
        assert todo2.id in todo_ids

    def test_list_todos_returns_empty_list_when_no_todos(self):
        """Test that listing todos returns an empty list when no todos exist."""
        todos = self.service.list_todos()

        assert todos == []

    def test_update_todo_updates_title(self):
        """Test that updating a todo updates its title."""
        original_todo = Todo.create(title="Original task")
        self.repository.save(original_todo)

        new_title = "Updated task"
        result = self.service.update_todo(original_todo.id, title=new_title)

        assert result is not None
        assert result.title == new_title

        # Verify the change is persisted
        updated_todo = self.repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.title == new_title

    def test_update_todo_updates_completion_status(self):
        """Test that updating a todo updates its completion status."""
        original_todo = Todo.create(title="Test task", completed=False)
        self.repository.save(original_todo)

        result = self.service.update_todo(original_todo.id, completed=True)

        assert result is not None
        assert result.completed is True

        # Verify the change is persisted
        updated_todo = self.repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is True

    def test_update_todo_updates_both_fields(self):
        """Test that updating a todo can update both title and completion status."""
        original_todo = Todo.create(title="Original task", completed=False)
        self.repository.save(original_todo)

        new_title = "Updated task"
        result = self.service.update_todo(original_todo.id, title=new_title, completed=True)

        assert result is not None
        assert result.title == new_title
        assert result.completed is True

        # Verify the changes are persisted
        updated_todo = self.repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.title == new_title
        assert updated_todo.completed is True

    def test_update_todo_returns_none_for_nonexistent_todo(self):
        """Test that updating a non-existent todo returns None."""
        result = self.service.update_todo("nonexistent-id", title="New title")

        assert result is None

    def test_update_todo_fails_with_invalid_title(self):
        """Test that updating a todo with invalid title raises ValueError."""
        original_todo = Todo.create(title="Test task")
        self.repository.save(original_todo)

        with pytest.raises(ValueError):
            self.service.update_todo(original_todo.id, title="")

    def test_delete_todo_removes_todo(self):
        """Test that deleting a todo removes it from the repository."""
        original_todo = Todo.create(title="Task to delete")
        self.repository.save(original_todo)

        result = self.service.delete_todo(original_todo.id)

        assert result is True
        assert self.repository.exists(original_todo.id) is False

    def test_delete_todo_returns_false_for_nonexistent_todo(self):
        """Test that deleting a non-existent todo returns False."""
        result = self.service.delete_todo("nonexistent-id")

        assert result is False

    def test_toggle_completion_toggles_status(self):
        """Test that toggling completion status changes the status."""
        original_todo = Todo.create(title="Test task", completed=False)
        self.repository.save(original_todo)

        # Toggle to completed
        result = self.service.toggle_completion(original_todo.id)

        assert result is not None
        assert result.completed is True

        # Verify the change is persisted
        updated_todo = self.repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is True

    def test_toggle_completion_returns_none_for_nonexistent_todo(self):
        """Test that toggling completion for a non-existent todo returns None."""
        result = self.service.toggle_completion("nonexistent-id")

        assert result is None

    def test_toggle_completion_can_toggle_back_to_false(self):
        """Test that toggling completion can switch from True to False."""
        original_todo = Todo.create(title="Test task", completed=True)
        self.repository.save(original_todo)

        # Toggle to incomplete
        result = self.service.toggle_completion(original_todo.id)

        assert result is not None
        assert result.completed is False

        # Verify the change is persisted
        updated_todo = self.repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is False