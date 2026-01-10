# In-Memory Python Console Todo App (Phase I)

This is a console-based todo application that stores tasks in memory. It supports the basic operations of adding, viewing, updating, deleting, and marking todos as complete/incomplete.

## Features

- Add new todo items
- View all todo items with their completion status
- Update existing todo descriptions
- Delete todo items
- Mark todos as complete or incomplete
- All data stored in memory only (no persistence)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies: `pip install -e .` (optional, for development)

## Usage

Run the application using one of the following methods:

```bash
# Method 1: Direct Python execution
python main.py

# Method 2: Using Python module execution
python -m src.todo_app.interface.cli
```

## Functionality

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

## Architecture

The application follows a layered architecture:

- **Domain Layer**: Contains the Todo entity and business logic
- **Application Layer**: Contains services and repositories for business operations
- **Interface Layer**: Contains the CLI interface for user interaction

## Testing

To run the tests:

```bash
# Run all tests
python -m pytest tests/

# Run tests with verbose output
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=src.todo_app
```

## Constraints

- All data is stored in memory only and will be lost when the application exits
- No external dependencies beyond Python standard library
- Console-based interface only
- Single-user application