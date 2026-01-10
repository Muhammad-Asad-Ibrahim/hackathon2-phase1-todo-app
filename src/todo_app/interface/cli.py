# """
# Command-line interface for the Todo application.
# """
# from ..application.services import TodoService


# class TodoCLI:
#     """
#     Command-line interface for interacting with the todo application.
#     """

#     def __init__(self, todo_service: TodoService):
#         self.todo_service = todo_service

#     def run(self):
#         print("Welcome to the Todo Application!")

#         while True:
#             self.display_menu()
#             choice = input("Choose an option: ").strip()

#             if choice == "1":
#                 self.add_todo()
#             elif choice == "2":
#                 self.view_todos()
#             elif choice == "3":
#                 self.update_todo()
#             elif choice == "4":
#                 self.delete_todo()
#             elif choice == "5":
#                 self.mark_todo_complete_incomplete()
#             elif choice == "6":
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Invalid option. Please choose again.")

#     def display_menu(self):
#         print("\nTodo Application")
#         print("1. Add Todo")
#         print("2. View Todos")
#         print("3. Update Todo")
#         print("4. Delete Todo")
#         print("5. Mark Todo as Complete/Incomplete")
#         print("6. Exit")

#     def add_todo(self):
#         title = input("Enter todo description: ").strip()
#         if not title:
#             print("Error: Todo description cannot be empty.")
#             return
#         if len(title) > 1000:
#             print("Error: Todo description cannot exceed 1000 characters.")
#             return

#         todo = self.todo_service.add_todo(title)
#         print(f"Todo added successfully with ID: {todo.id}")

#     def view_todos(self):
#         todos = self.todo_service.list_todos()
#         if not todos:
#             print("No todos found.")
#             return

#         print("Todos:")
#         for todo in todos:
#             status = "[x]" if todo.completed else "[ ]"
#             print(f"ID: {todo.id} - {status} {todo.title}")

#     def update_todo(self):
#         todo_id = input("Enter todo ID to update: ").strip()
#         if not todo_id.isdigit():
#             print("Error: Todo ID must be a number.")
#             return
#         todo_id = int(todo_id)

#         existing_todo = self.todo_service.get_todo(todo_id)
#         if not existing_todo:
#             print(f"Error: Todo with ID '{todo_id}' not found.")
#             return

#         new_title = input(f"Enter new description (current: '{existing_todo.title}'): ").strip()
#         if not new_title:
#             print("No changes made.")
#             return
#         if len(new_title) > 1000:
#             print("Error: Todo description cannot exceed 1000 characters.")
#             return

#         updated = self.todo_service.update_todo(todo_id, title=new_title)
#         if updated:
#             print("Todo updated successfully.")
#         else:
#             print(f"Error: Todo with ID '{todo_id}' could not be updated.")

#     def delete_todo(self):
#         todo_id = input("Enter todo ID to delete: ").strip()
#         if not todo_id.isdigit():
#             print("Error: Todo ID must be a number.")
#             return
#         todo_id = int(todo_id)

#         if self.todo_service.delete_todo(todo_id):
#             print("Todo deleted successfully.")
#         else:
#             print(f"Error: Todo with ID '{todo_id}' not found.")

#     def mark_todo_complete_incomplete(self):
#         todo_id = input("Enter todo ID to toggle completion: ").strip()
#         if not todo_id.isdigit():
#             print("Error: Todo ID must be a number.")
#             return
#         todo_id = int(todo_id)

#         todo = self.todo_service.toggle_completion(todo_id)
#         if todo:
#             status = "completed" if todo.completed else "incomplete"
#             print(f"Todo marked as {status}.")
#         else:
#             print(f"Error: Todo with ID '{todo_id}' not found.")


# def main():
#     from ..application.repositories import InMemoryTodoRepository

#     repository = InMemoryTodoRepository()
#     service = TodoService(repository)

#     cli = TodoCLI(service)
#     cli.run()


# if __name__ == "__main__":
#     main()



"""
Command-line interface for the Todo application.
"""
from ..application.services import TodoService


class TodoCLI:
    """
    Command-line interface for interacting with the todo application.
    """

    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def run(self):
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.view_todos()
            elif choice == "3":
                self.update_todo()
            elif choice == "4":
                self.delete_todo()
            elif choice == "5":
                self.mark_todo_complete()
            elif choice == "6":
                self.mark_todo_incomplete()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")

    def display_menu(self):
        print("\nTodo Application")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Todo as Complete")
        print("6. Mark Todo as Incomplete")
        print("7. Exit")

    def add_todo(self):
        title = input("Enter todo description: ").strip()
        if not title:
            print("Error: Todo description cannot be empty.")
            return
        if len(title) > 1000:
            print("Error: Todo description cannot exceed 1000 characters.")
            return

        todo = self.todo_service.add_todo(title)
        print(f"Todo added successfully with ID: {todo.id}")

    def view_todos(self):
        todos = self.todo_service.list_todos()
        if not todos:
            print("No todos found.")
            return

        print("Todos:")
        for todo in todos:
            status = "[x]" if todo.completed else "[ ]"
            print(f"ID: {todo.id} - {status} {todo.title}")

    def update_todo(self):
        todo_id = input("Enter todo ID to update: ").strip()
        if not todo_id.isdigit():
            print("Error: Todo ID must be a number.")
            return
        todo_id = int(todo_id)

        existing_todo = self.todo_service.get_todo(todo_id)
        if not existing_todo:
            print(f"Error: Todo with ID '{todo_id}' not found.")
            return

        new_title = input(f"Enter new description (current: '{existing_todo.title}'): ").strip()
        if not new_title:
            print("No changes made.")
            return
        if len(new_title) > 1000:
            print("Error: Todo description cannot exceed 1000 characters.")
            return

        updated = self.todo_service.update_todo(todo_id, title=new_title)
        if updated:
            print("Todo updated successfully.")
        else:
            print(f"Error: Todo with ID '{todo_id}' could not be updated.")

    def delete_todo(self):
        todo_id = input("Enter todo ID to delete: ").strip()
        if not todo_id.isdigit():
            print("Error: Todo ID must be a number.")
            return
        todo_id = int(todo_id)

        if self.todo_service.delete_todo(todo_id):
            print("Todo deleted successfully.")
        else:
            print(f"Error: Todo with ID '{todo_id}' not found.")

    def mark_todo_complete(self):
        todo_id = input("Enter todo ID to mark as complete: ").strip()
        if not todo_id.isdigit():
            print("Error: Todo ID must be a number.")
            return
        todo_id = int(todo_id)

        todo = self.todo_service.update_todo(todo_id, completed=True)
        if todo:
            print(f"Todo ID {todo_id} marked as completed.")
        else:
            print(f"Error: Todo with ID '{todo_id}' not found.")

    def mark_todo_incomplete(self):
        todo_id = input("Enter todo ID to mark as incomplete: ").strip()
        if not todo_id.isdigit():
            print("Error: Todo ID must be a number.")
            return
        todo_id = int(todo_id)

        todo = self.todo_service.update_todo(todo_id, completed=False)
        if todo:
            print(f"Todo ID {todo_id} marked as incomplete.")
        else:
            print(f"Error: Todo with ID '{todo_id}' not found.")


def main():
    from ..application.repositories import InMemoryTodoRepository

    repository = InMemoryTodoRepository()
    service = TodoService(repository)

    cli = TodoCLI(service)
    cli.run()


if __name__ == "__main__":
    main()
