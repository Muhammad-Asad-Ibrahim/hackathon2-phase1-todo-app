# Quickstart Guide: In-Memory Python Console Todo App (Phase I)

**Feature**: 1-in-memory-todo
**Date**: 2026-01-09

## Prerequisites

- Python 3.13 or higher
- UV package manager (for dependency management)

## Setup

1. **Clone or create the project structure**:
   ```bash
   mkdir todo-app
   cd todo-app
   ```

2. **Initialize the project with UV**:
   ```bash
   uv init
   ```

3. **Create the source directory structure**:
   ```bash
   mkdir -p src/todo_app/{domain,application,interface}
   ```

## Running the Application

1. **Install dependencies** (if any are added later):
   ```bash
   uv sync
   ```

2. **Run the application**:
   ```bash
   python -m src.todo_app.interface.cli
   ```

## Development Commands

1. **Run tests**:
   ```bash
   python -m pytest tests/
   ```

2. **Run specific test file**:
   ```bash
   python -m pytest tests/unit/domain/test_models.py
   ```

3. **Run all tests with coverage**:
   ```bash
   python -m pytest --cov=src.todo_app
   ```

## Application Usage

Once the application is running, you'll see a menu with the following options:

```
Todo Application
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo as Complete/Incomplete
6. Exit
Choose an option:
```

### Available Commands

- **Option 1**: Add a new todo by entering its description
- **Option 2**: View all todos with their completion status
- **Option 3**: Update an existing todo by specifying its ID and new description
- **Option 4**: Delete a todo by specifying its ID
- **Option 5**: Toggle the completion status of a todo by specifying its ID
- **Option 6**: Exit the application (data will be lost)

## Example Session

```
Todo Application
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo as Complete/Incomplete
6. Exit
Choose an option: 1
Enter todo description: Buy groceries
Todo added successfully with ID: 1

Choose an option: 1
Enter todo description: Finish report
Todo added successfully with ID: 2

Choose an option: 2
Todos:
ID: 1 - [ ] Buy groceries
ID: 2 - [ ] Finish report

Choose an option: 5
Enter todo ID to toggle: 1
Todo status updated successfully

Choose an option: 2
Todos:
ID: 1 - [x] Buy groceries
ID: 2 - [ ] Finish report

Choose an option: 6
Goodbye!
```

## File Structure Reference

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models.py          # Todo data model
│   │   └── entities.py        # Todo entity definitions
│   ├── application/
│   │   ├── __init__.py
│   │   ├── services.py        # Todo operations (add, update, delete, complete)
│   │   └── repositories.py    # In-memory repository
│   └── interface/
│       ├── __init__.py
│       ├── cli.py             # Console input/output handling
│       └── commands.py        # Command processing
│
tests/
├── unit/
│   ├── domain/
│   ├── application/
│   └── interface/
├── integration/
└── conftest.py
```

## Troubleshooting

- If you get a "module not found" error, ensure you're running Python with the `-m` flag from the project root
- If the application doesn't start, verify Python 3.13+ is installed
- For any runtime errors, check the error message and verify input format matches expectations