"""
Unit tests for Todo entity.
"""
import pytest
from src.todo_app.domain.entities import Todo


class TestTodo:
    """Test cases for the Todo entity."""

    def test_create_todo_with_valid_data(self):
        """Test creating a todo with valid data."""
        title = "Buy groceries"
        todo = Todo.create(title=title)

        assert todo.id is not None
        assert todo.title == title
        assert todo.completed is False

    def test_create_todo_sets_completed_false_by_default(self):
        """Test that todo is not completed by default."""
        todo = Todo.create(title="Sample task")

        assert todo.completed is False

    def test_create_todo_with_custom_completion_status(self):
        """Test creating a todo with custom completion status."""
        todo = Todo.create(title="Sample task", completed=True)

        assert todo.completed is True

    def test_todo_validation_fails_with_empty_title(self):
        """Test that creating a todo with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Todo title cannot be empty or only whitespace"):
            Todo.create(title="")

    def test_todo_validation_fails_with_whitespace_only_title(self):
        """Test that creating a todo with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Todo title cannot be empty or only whitespace"):
            Todo.create(title="   ")

    def test_todo_validation_fails_with_long_title(self):
        """Test that creating a todo with overly long title raises ValueError."""
        long_title = "x" * 1001  # Exceeds 1000 character limit
        with pytest.raises(ValueError, match="Todo title cannot exceed 1000 characters"):
            Todo.create(title=long_title)

    def test_update_title_successfully(self):
        """Test updating the title of a todo."""
        todo = Todo.create(title="Old title")

        new_title = "New title"
        todo.update_title(new_title)

        assert todo.title == new_title

    def test_update_title_fails_with_empty_string(self):
        """Test that updating title with empty string raises ValueError."""
        todo = Todo.create(title="Valid title")

        with pytest.raises(ValueError, match="Todo title cannot be empty or only whitespace"):
            todo.update_title("")

    def test_update_title_fails_with_whitespace_only(self):
        """Test that updating title with whitespace-only string raises ValueError."""
        todo = Todo.create(title="Valid title")

        with pytest.raises(ValueError, match="Todo title cannot be empty or only whitespace"):
            todo.update_title("   ")

    def test_update_title_fails_with_long_string(self):
        """Test that updating title with overly long string raises ValueError."""
        todo = Todo.create(title="Valid title")
        long_title = "x" * 1001  # Exceeds 1000 character limit

        with pytest.raises(ValueError, match="Todo title cannot exceed 1000 characters"):
            todo.update_title(long_title)

    def test_toggle_completion_changes_status(self):
        """Test that toggling completion status changes the status."""
        todo = Todo.create(title="Sample task", completed=False)

        # Initially not completed
        assert todo.completed is False

        # Toggle to completed
        todo.toggle_completion()
        assert todo.completed is True

        # Toggle back to incomplete
        todo.toggle_completion()
        assert todo.completed is False