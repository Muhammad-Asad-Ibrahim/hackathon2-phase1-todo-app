"""
Application service for todo operations.
"""
from typing import List, Optional
from ..domain.entities import Todo
from .repositories import InMemoryTodoRepository


class TodoService:
    """
    Service class for managing todo operations.

    This service orchestrates domain operations and interacts with the repository.
    """

    def __init__(self, repository: InMemoryTodoRepository):
        """
        Initialize the service with a repository.

        Args:
            repository: The repository to use for data operations
        """
        self.repository = repository

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo with the given title.

        Args:
            title: The title of the new todo

        Returns:
            The created Todo object

        Raises:
            ValueError: If the title is invalid
        """
        # Create a new todo with the given title
        todo = Todo.create(title=title)

        # Save the todo to the repository
        self.repository.save(todo)

        return todo

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo if found, None otherwise
        """
        return self.repository.find_by_id(todo_id)

    def list_todos(self) -> List[Todo]:
        """
        List all todos.

        Returns:
            List of all todos
        """
        return self.repository.find_all()

    def update_todo(self, todo_id: str, title: Optional[str] = None, completed: Optional[bool] = None) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            todo_id: The ID of the todo to update
            title: New title for the todo (optional)
            completed: New completion status (optional)

        Returns:
            The updated todo if successful, None if todo doesn't exist

        Raises:
            ValueError: If the new title is invalid
        """
        # Get the existing todo
        existing_todo = self.repository.find_by_id(todo_id)
        if existing_todo is None:
            return None

        # Update the todo's attributes if provided
        if title is not None:
            existing_todo.update_title(title)

        if completed is not None:
            existing_todo.completed = completed

        # Save the updated todo back to the repository
        self.repository.update(existing_todo)

        return existing_todo

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if deletion was successful, False if todo didn't exist
        """
        return self.repository.delete_by_id(todo_id)

    def toggle_completion(self, todo_id: str) -> Optional[Todo]:
        """
        Toggle the completion status of a todo.

        Args:
            todo_id: The ID of the todo to toggle

        Returns:
            The updated todo if successful, None if todo doesn't exist
        """
        # Get the existing todo
        existing_todo = self.repository.find_by_id(todo_id)
        if existing_todo is None:
            return None

        # Toggle the completion status
        existing_todo.toggle_completion()

        # Save the updated todo back to the repository
        self.repository.update(existing_todo)

        return existing_todo