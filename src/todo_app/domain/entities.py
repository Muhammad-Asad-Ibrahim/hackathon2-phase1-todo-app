"""
Todo entity definition.
"""
from dataclasses import dataclass
from typing import Optional
import uuid


@dataclass
class Todo:
    """
    Represents a single todo item.

    Attributes:
        id (str): Unique identifier for the todo
        title (str): Description of the task to be completed
        completed (bool): Status indicating completion state
    """
    id: str
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        self._validate()

    def _validate(self):
        """Validate the todo attributes."""
        if not self.title or not self.title.strip():
            raise ValueError("Todo title cannot be empty or only whitespace")

        if len(self.title) > 1000:
            raise ValueError("Todo title cannot exceed 1000 characters")

        if not isinstance(self.completed, bool):
            raise TypeError("Todo completed status must be a boolean")

    @classmethod
    def create(cls, title: str, completed: bool = False) -> 'Todo':
        """
        Create a new Todo with a generated ID.

        Args:
            title: Description of the task to be completed
            completed: Whether the task is completed (default: False)

        Returns:
            Todo: New Todo instance with generated ID
        """
        todo_id = str(uuid.uuid4())
        return cls(id=todo_id, title=title.strip(), completed=completed)

    def update_title(self, new_title: str):
        """
        Update the title of the todo.

        Args:
            new_title: New title for the todo
        """
        stripped_title = new_title.strip()
        if not stripped_title:
            raise ValueError("Todo title cannot be empty or only whitespace")

        if len(stripped_title) > 1000:
            raise ValueError("Todo title cannot exceed 1000 characters")

        self.title = stripped_title

    def toggle_completion(self):
        """Toggle the completion status of the todo."""
        self.completed = not self.completed