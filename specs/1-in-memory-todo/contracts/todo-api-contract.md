# Todo API Contract: In-Memory Python Console Todo App (Phase I)

**Feature**: 1-in-memory-todo
**Date**: 2026-01-09

## Overview

This contract defines the interface for the todo application services. Although this is a console application, we define the logical operations that the application service layer will provide.

## Service Interface: TodoService

### Methods

#### 1. add_todo(title: str) -> dict
**Description**: Creates a new todo item with the provided title.

**Parameters**:
- `title` (str): The description of the task to be completed

**Returns**:
- `dict`: Object containing the created todo with structure:
  ```json
  {
    "id": "unique_identifier",
    "title": "task description",
    "completed": false
  }
  ```

**Preconditions**:
- `title` must not be empty or consist only of whitespace

**Postconditions**:
- New todo is added to the in-memory collection
- Todo is initially marked as incomplete

**Exceptions**:
- `ValueError` if title is empty or only whitespace

#### 2. get_todo(todo_id: str) -> dict
**Description**: Retrieves a specific todo by its ID.

**Parameters**:
- `todo_id` (str): The unique identifier of the todo

**Returns**:
- `dict`: Todo object with structure:
  ```json
  {
    "id": "unique_identifier",
    "title": "task description",
    "completed": true/false
  }
  ```

**Preconditions**:
- `todo_id` must exist in the collection

**Exceptions**:
- `KeyError` if todo_id does not exist

#### 3. list_todos() -> list[dict]
**Description**: Retrieves all todos in the collection.

**Returns**:
- `list[dict]`: Array of todo objects with the same structure as above

**Postconditions**:
- Returns empty array if no todos exist

#### 4. update_todo(todo_id: str, title: str = None, completed: bool = None) -> dict
**Description**: Updates properties of an existing todo.

**Parameters**:
- `todo_id` (str): The unique identifier of the todo
- `title` (str, optional): New title for the todo
- `completed` (bool, optional): New completion status

**Returns**:
- `dict`: Updated todo object

**Preconditions**:
- `todo_id` must exist in the collection
- If `title` is provided, it must not be empty or consist only of whitespace

**Postconditions**:
- Specified properties are updated in the todo
- Other properties remain unchanged

**Exceptions**:
- `KeyError` if todo_id does not exist
- `ValueError` if title is empty or only whitespace

#### 5. delete_todo(todo_id: str) -> bool
**Description**: Removes a todo from the collection.

**Parameters**:
- `todo_id` (str): The unique identifier of the todo

**Returns**:
- `bool`: True if deletion was successful, False if todo didn't exist

**Postconditions**:
- Todo is removed from the collection
- Associated resources are freed

#### 6. toggle_completion(todo_id: str) -> dict
**Description**: Toggles the completion status of a todo.

**Parameters**:
- `todo_id` (str): The unique identifier of the todo

**Returns**:
- `dict`: Updated todo object with toggled completion status

**Preconditions**:
- `todo_id` must exist in the collection

**Postconditions**:
- Todo's completion status is flipped (true becomes false, false becomes true)

**Exceptions**:
- `KeyError` if todo_id does not exist

## Repository Interface: TodoRepository

### Methods

#### 1. save(todo: dict) -> None
**Description**: Saves a todo to the in-memory collection.

**Parameters**:
- `todo` (dict): The todo object to save

#### 2. find_by_id(todo_id: str) -> dict
**Description**: Finds a todo by its ID.

**Parameters**:
- `todo_id` (str): The unique identifier to search for

**Returns**:
- `dict`: The found todo object

**Exceptions**:
- `KeyError` if not found

#### 3. find_all() -> list[dict]
**Description**: Retrieves all todos in the collection.

**Returns**:
- `list[dict]`: Array of all todo objects

#### 4. delete_by_id(todo_id: str) -> bool
**Description**: Deletes a todo by its ID.

**Parameters**:
- `todo_id` (str): The unique identifier of the todo to delete

**Returns**:
- `bool`: True if deletion was successful, False if todo didn't exist

#### 5. exists(todo_id: str) -> bool
**Description**: Checks if a todo exists in the collection.

**Parameters**:
- `todo_id` (str): The unique identifier to check

**Returns**:
- `bool`: True if exists, False otherwise