"""
Unit tests for InMemoryTodoRepository.
"""
import pytest
from src.todo_app.domain.entities import Todo
from src.todo_app.application.repositories import InMemoryTodoRepository


class TestInMemoryTodoRepository:
    """Test cases for the InMemoryTodoRepository."""

    def test_save_and_find_by_id(self):
        """Test saving a todo and retrieving it by ID."""
        repository = InMemoryTodoRepository()
        todo = Todo.create(title="Test task")

        repository.save(todo)
        retrieved_todo = repository.find_by_id(todo.id)

        assert retrieved_todo is not None
        assert retrieved_todo.id == todo.id
        assert retrieved_todo.title == todo.title
        assert retrieved_todo.completed == todo.completed

    def test_find_by_id_returns_none_for_nonexistent_todo(self):
        """Test that finding a non-existent todo returns None."""
        repository = InMemoryTodoRepository()

        result = repository.find_by_id("nonexistent-id")

        assert result is None

    def test_find_all_returns_empty_list_when_no_todos(self):
        """Test that find_all returns an empty list when no todos exist."""
        repository = InMemoryTodoRepository()

        todos = repository.find_all()

        assert todos == []

    def test_find_all_returns_all_todos(self):
        """Test that find_all returns all saved todos."""
        repository = InMemoryTodoRepository()
        todo1 = Todo.create(title="Task 1")
        todo2 = Todo.create(title="Task 2")

        repository.save(todo1)
        repository.save(todo2)

        todos = repository.find_all()

        assert len(todos) == 2
        todo_ids = {todo.id for todo in todos}
        assert todo1.id in todo_ids
        assert todo2.id in todo_ids

    def test_delete_by_id_removes_todo(self):
        """Test that deleting a todo removes it from the repository."""
        repository = InMemoryTodoRepository()
        todo = Todo.create(title="Task to delete")

        repository.save(todo)
        assert repository.exists(todo.id) is True

        result = repository.delete_by_id(todo.id)
        assert result is True
        assert repository.exists(todo.id) is False

    def test_delete_by_id_returns_false_for_nonexistent_todo(self):
        """Test that deleting a non-existent todo returns False."""
        repository = InMemoryTodoRepository()

        result = repository.delete_by_id("nonexistent-id")

        assert result is False

    def test_exists_returns_true_for_existing_todo(self):
        """Test that exists returns True for an existing todo."""
        repository = InMemoryTodoRepository()
        todo = Todo.create(title="Test task")

        repository.save(todo)

        assert repository.exists(todo.id) is True

    def test_exists_returns_false_for_nonexistent_todo(self):
        """Test that exists returns False for a non-existent todo."""
        repository = InMemoryTodoRepository()

        assert repository.exists("nonexistent-id") is False

    def test_update_modifies_existing_todo(self):
        """Test that updating a todo modifies its properties."""
        repository = InMemoryTodoRepository()
        original_todo = Todo.create(title="Original task", completed=False)

        repository.save(original_todo)

        # Modify the todo
        original_todo.update_title("Updated task")
        original_todo.completed = True

        # Update in repository
        repository.update(original_todo)

        # Retrieve and verify changes
        updated_todo = repository.find_by_id(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.title == "Updated task"
        assert updated_todo.completed is True

    def test_update_does_not_affect_nonexistent_todo(self):
        """Test that updating a non-existent todo doesn't cause errors."""
        repository = InMemoryTodoRepository()
        todo = Todo.create(title="Test task")
        # Don't save this todo to the repository

        # This should not raise an exception but also not persist anything
        repository.update(todo)

        # The todo should not exist in the repository
        assert repository.exists(todo.id) is False