# In-Memory Python Console Todo App (Phase I)

This is a console-based todo application built using Python. The application stores all tasks in memory and allows users to manage their todos through a command-line interface.

---

## Features

- Add new todo items
- View all todo items with completion status
- Update existing todo descriptions
- Delete todo items
- Mark todos as complete
- Mark todos as incomplete
- In-memory storage (no data persistence)

---

## Requirements

- Python 3.13 or higher

---

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. (Optional) Install the project in editable mode:
   ```bash
   pip install -e .


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
5. Mark Todo as Complete
6. Mark Todo as Incomplete
7. Exit
Choose an option:
```

### Available Commands

- **Option 1**: Add a new todo by entering its description
- **Option 2**: View all todos with their completion status
- **Option 3**: Update an existing todo by specifying its ID and new description
- **Option 4**: Delete a todo by specifying its ID
- **Option 5**: Marks the selected todo as completed 
- **Option 6**: Marks the selected todo as incomplete
- **Option 7**: Exit the application (data will be lost)
  
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
