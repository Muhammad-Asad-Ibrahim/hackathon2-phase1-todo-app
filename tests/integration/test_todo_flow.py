"""
Integration tests for the todo application flow.
"""
import pytest
from src.todo_app.domain.entities import Todo
from src.todo_app.application.repositories import InMemoryTodoRepository
from src.todo_app.application.services import TodoService


class TestTodoFlow:
    """Integration tests for the complete todo flow."""

    def setup_method(self):
        """Set up a fresh repository and service for each test."""
        self.repository = InMemoryTodoRepository()
        self.service = TodoService(self.repository)

    def test_complete_todo_lifecycle(self):
        """Test the complete lifecycle of a todo: add, view, update, mark complete, delete."""
        # Step 1: Add a new todo
        title = "Complete integration test"
        added_todo = self.service.add_todo(title)

        assert added_todo is not None
        assert added_todo.id is not None
        assert added_todo.title == title
        assert added_todo.completed is False

        # Step 2: Verify it's in the list
        all_todos = self.service.list_todos()
        assert len(all_todos) == 1
        retrieved_todo = all_todos[0]
        assert retrieved_todo.id == added_todo.id
        assert retrieved_todo.title == title
        assert retrieved_todo.completed is False

        # Step 3: Update the todo
        new_title = "Updated integration test"
        updated_todo = self.service.update_todo(added_todo.id, title=new_title)

        assert updated_todo is not None
        assert updated_todo.title == new_title
        assert updated_todo.completed is False  # Completion should remain unchanged

        # Step 4: Verify the update in the list
        all_todos = self.service.list_todos()
        assert len(all_todos) == 1
        retrieved_todo = all_todos[0]
        assert retrieved_todo.title == new_title

        # Step 5: Mark as complete
        completed_todo = self.service.toggle_completion(added_todo.id)

        assert completed_todo is not None
        assert completed_todo.completed is True

        # Step 6: Verify the completion in the list
        all_todos = self.service.list_todos()
        assert len(all_todos) == 1
        retrieved_todo = all_todos[0]
        assert retrieved_todo.completed is True

        # Step 7: Delete the todo
        delete_result = self.service.delete_todo(added_todo.id)

        assert delete_result is True

        # Step 8: Verify it's gone from the list
        all_todos = self.service.list_todos()
        assert len(all_todos) == 0

    def test_multiple_todos_management(self):
        """Test managing multiple todos simultaneously."""
        # Add multiple todos
        todo1 = self.service.add_todo("First task")
        todo2 = self.service.add_todo("Second task")
        todo3 = self.service.add_todo("Third task")

        # Verify all exist
        all_todos = self.service.list_todos()
        assert len(all_todos) == 3

        # Mark the second one as complete
        completed_todo = self.service.toggle_completion(todo2.id)
        assert completed_todo is not None
        assert completed_todo.completed is True

        # Update the first one
        updated_todo = self.service.update_todo(todo1.id, title="Updated first task")
        assert updated_todo is not None
        assert updated_todo.title == "Updated first task"

        # Verify the state of all todos
        all_todos = self.service.list_todos()
        assert len(all_todos) == 3

        # Find each todo and verify its state
        todo_dict = {todo.id: todo for todo in all_todos}

        # First todo: updated title, incomplete
        assert todo_dict[todo1.id].title == "Updated first task"
        assert not todo_dict[todo1.id].completed

        # Second todo: original title, completed
        assert todo_dict[todo2.id].title == "Second task"
        assert todo_dict[todo2.id].completed

        # Third todo: original title, incomplete
        assert todo_dict[todo3.id].title == "Third task"
        assert not todo_dict[todo3.id].completed

    def test_view_empty_list(self):
        """Test viewing an empty todo list."""
        todos = self.service.list_todos()
        assert len(todos) == 0
        assert todos == []

    def test_operations_on_nonexistent_todos(self):
        """Test that operations on non-existent todos return appropriate values."""
        # Attempt to get a non-existent todo
        nonexistent_todo = self.service.get_todo("nonexistent-id")
        assert nonexistent_todo is None

        # Attempt to update a non-existent todo
        updated_todo = self.service.update_todo("nonexistent-id", title="New title")
        assert updated_todo is None

        # Attempt to delete a non-existent todo
        delete_result = self.service.delete_todo("nonexistent-id")
        assert delete_result is False

        # Attempt to toggle completion of a non-existent todo
        toggled_todo = self.service.toggle_completion("nonexistent-id")
        assert toggled_todo is None