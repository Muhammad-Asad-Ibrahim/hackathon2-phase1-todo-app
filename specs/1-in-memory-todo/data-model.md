# Data Model: In-Memory Python Console Todo App (Phase I)

**Feature**: 1-in-memory-todo
**Date**: 2026-01-09

## Todo Entity

### Fields
- **id** (str/UUID): Unique identifier for each todo item
  - Auto-generated when creating new todos
  - Immutable after creation
  - Used for referencing in operations

- **title** (str): Description of the task to be completed
  - Required field (cannot be empty)
  - Can contain any printable characters
  - Maximum length: 1000 characters (configurable)

- **completed** (bool): Status indicating completion state
  - Default: False (incomplete)
  - Can be toggled between True (complete) and False (incomplete)

### Relationships
- No direct relationships with other entities in this phase
- Belongs to a TodoList collection in memory

### Validation Rules
1. **Title cannot be empty**: Must contain at least one non-whitespace character
2. **Title length limit**: Maximum 1000 characters to prevent excessive memory usage
3. **ID uniqueness**: Each todo must have a unique identifier
4. **ID immutability**: Once created, a todo's ID cannot be changed
5. **Status validity**: Completed field must be boolean (True/False)

## TodoList Collection

### Structure
- **Internal representation**: Dictionary mapping IDs to Todo objects
  - Key: todo.id (str)
  - Value: Todo object instance

### Operations Supported
1. **Add**: Insert a new Todo with auto-generated ID
2. **Get**: Retrieve a Todo by ID
3. **Update**: Modify an existing Todo's properties
4. **Delete**: Remove a Todo by ID
5. **List All**: Retrieve all Todos in the collection
6. **Filter**: Get all completed or incomplete Todos

### State Transitions
- **New Todo**: `completed = False` by default
- **Complete Todo**: `completed = True` when marked complete
- **Reopen Todo**: `completed = False` when marked incomplete

### Constraints
1. **Memory-only storage**: Contents exist only in application memory
2. **No persistence**: Data is lost when application terminates
3. **Thread safety**: Not required for single-user console application
4. **Order preservation**: Order of insertion maintained in list operations

## Domain Invariants
1. **Completeness**: Every Todo has a defined completion status
2. **Non-emptiness**: Todo titles cannot become empty after creation
3. **Identity**: Each Todo maintains a consistent identity via its ID
4. **Validity**: All Todo objects satisfy validation rules at all times