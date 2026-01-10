"""
In-memory repository for todo items.
"""
from typing import Dict, List, Optional
from ..domain.entities import Todo


class InMemoryTodoRepository:
    """
    In-memory repository for managing todo items.
    """

    def __init__(self):
        """Initialize the repository with an empty collection."""
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1   # 👈 NEW

    def save(self, todo: Todo) -> Todo:
        """
        Save a todo to the repository.
        Auto-assigns an integer ID.
        """
        todo.id = self._next_id
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def find_by_id(self, todo_id: int) -> Optional[Todo]:
        return self._todos.get(todo_id)

    def find_all(self) -> List[Todo]:
        return list(self._todos.values())

    def delete_by_id(self, todo_id: int) -> bool:
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False

    def exists(self, todo_id: int) -> bool:
        return todo_id in self._todos

    def update(self, todo: Todo) -> None:
        if todo.id in self._todos:
            self._todos[todo.id] = todo
