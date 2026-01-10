"""
Main entry point for the Todo Application.
"""
from src.todo_app.application.repositories import InMemoryTodoRepository
from src.todo_app.application.services import TodoService
from src.todo_app.interface.cli import TodoCLI


def main():
    """
    Main function to run the Todo Application.
    """
    # Initialize the repository and service
    repository = InMemoryTodoRepository()
    service = TodoService(repository)

    # Initialize and run the CLI
    cli = TodoCLI(service)
    cli.run()


if __name__ == "__main__":
    main()