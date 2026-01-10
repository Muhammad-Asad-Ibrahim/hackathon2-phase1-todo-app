# Tasks: In-Memory Python Console Todo App (Phase I)

**Feature**: 1-in-memory-todo
**Date**: 2026-01-09
**Branch**: 1-in-memory-todo

## Overview

This document outlines all tasks for implementing the In-Memory Python Console Todo App (Phase I). Tasks are organized by user story priority and follow the layered architecture approach.

## Dependencies

User stories can be implemented independently but share foundational components:
- US2 (View Todos) depends on US1 (Add Todos) for data to display
- US3-5 (Update, Delete, Mark Complete/Incomplete) depend on US1 for data to operate on

## Parallel Execution Examples

- T001-T005 can be worked on in parallel by different developers
- Domain models can be developed in parallel with repository implementations
- Unit tests can be written in parallel with implementation

## Implementation Strategy

- MVP includes US1 (Add Todo) and basic CLI interface
- Each user story builds incrementally on the previous
- Focus on core functionality first, then error handling and edge cases

---

## Phase 1: Setup

Goal: Initialize project structure and foundational components

- [X] T001 Create project directory structure per quickstart guide
- [X] T002 Initialize Python project with UV
- [X] T003 Set up basic configuration files (pyproject.toml, etc.)
- [X] T004 Create source directory structure: src/todo_app/{domain,application,interface}
- [X] T005 Set up test directory structure: tests/{unit,integration}/{domain,application,interface}

## Phase 2: Foundation

Goal: Create core components that all user stories depend on

- [X] T006 [P] Create domain models module: src/todo_app/domain/__init__.py
- [X] T007 [P] Create application services module: src/todo_app/application/__init__.py
- [X] T008 [P] Create interface module: src/todo_app/interface/__init__.py
- [X] T009 [P] Create tests conftest.py: tests/conftest.py
- [X] T010 [P] Set up pytest configuration

## Phase 3: User Story 1 - Add Todo Items (Priority: P1)

Goal: Enable users to add new tasks to their todo list through the console interface

Independent Test: User can enter a todo description and verify it appears in the list, delivering the core value of task storage.

**Acceptance**:
1. Given an empty todo list, when user adds a new task "Buy groceries", then the task appears in the list with a unique identifier
2. Given a non-empty todo list, when user adds another task "Finish report", then the new task is added to the list without affecting existing tasks

- [X] T011 [P] [US1] Create Todo entity class in src/todo_app/domain/entities.py
- [X] T012 [P] [US1] Implement Todo validation rules in src/todo_app/domain/entities.py
- [X] T013 [P] [US1] Create InMemoryTodoRepository in src/todo_app/application/repositories.py
- [X] T014 [P] [US1] Implement add_todo method in repository
- [X] T015 [US1] Create TodoService in src/todo_app/application/services.py
- [X] T016 [US1] Implement add_todo method in TodoService
- [X] T017 [P] [US1] Create CLI interface module: src/todo_app/interface/cli.py
- [X] T018 [US1] Implement basic command loop in cli.py
- [X] T019 [US1] Implement add todo command in cli.py
- [X] T020 [US1] Display menu with "Add Todo" option
- [X] T021 [P] [US1] Create unit tests for Todo entity
- [X] T022 [P] [US1] Create unit tests for InMemoryTodoRepository add functionality
- [X] T023 [P] [US1] Create unit tests for TodoService add functionality
- [X] T024 [US1] Create integration tests for add todo flow

## Phase 4: User Story 2 - View Todo Items (Priority: P1)

Goal: Enable users to see all their pending tasks in a clear, organized format

Independent Test: User can view the list of todos after adding them, delivering the core value of task visibility.

**Acceptance**:
1. Given a list of added todos, when user requests to view the list, then all todos are displayed with their status (complete/incomplete)
2. Given an empty todo list, when user requests to view the list, then a message indicates that there are no todos

- [X] T025 [P] [US2] Implement list_todos method in InMemoryTodoRepository
- [X] T026 [P] [US2] Implement get_todo method in InMemoryTodoRepository
- [X] T027 [US2] Implement list_todos method in TodoService
- [X] T028 [US2] Implement view todos command in cli.py
- [X] T029 [US2] Display menu with "View Todos" option
- [X] T030 [P] [US2] Create unit tests for repository list/get functionality
- [X] T031 [P] [US2] Create unit tests for TodoService list functionality
- [X] T032 [US2] Create integration tests for view todos flow

## Phase 5: User Story 3 - Mark Todo as Complete/Incomplete (Priority: P2)

Goal: Enable users to mark tasks as completed once they finish them, and potentially mark them as incomplete again

Independent Test: User can mark a todo as complete and then as incomplete, delivering the value of progress tracking.

**Acceptance**:
1. Given a list with an incomplete todo, when user marks it as complete, then the status updates and reflects as completed in the list
2. Given a list with a completed todo, when user marks it as incomplete, then the status updates and reflects as incomplete in the list

- [X] T033 [P] [US3] Implement toggle_completion method in InMemoryTodoRepository
- [X] T034 [P] [US3] Implement update_todo method in InMemoryTodoRepository
- [X] T035 [US3] Implement toggle_completion method in TodoService
- [X] T036 [US3] Implement mark todo complete/incomplete command in cli.py
- [X] T037 [US3] Display menu with "Mark Todo as Complete/Incomplete" option
- [X] T038 [P] [US3] Create unit tests for repository toggle/update functionality
- [X] T039 [P] [US3] Create unit tests for TodoService toggle functionality
- [X] T040 [US3] Create integration tests for mark todo flow

## Phase 6: User Story 4 - Update Todo Description (Priority: P2)

Goal: Enable users to modify the description of an existing todo if they need to clarify or change the task details

Independent Test: User can update a todo description and verify the change persists, delivering the value of task modification.

**Acceptance**:
1. Given a todo with a specific description, when user updates the description, then the new description is stored and displayed when viewing the list

- [X] T041 [P] [US4] Implement update_todo method in TodoService (enhanced)
- [X] T042 [US4] Implement update todo command in cli.py
- [X] T043 [US4] Display menu with "Update Todo" option
- [X] T044 [P] [US4] Create unit tests for TodoService update functionality
- [X] T045 [US4] Create integration tests for update todo flow

## Phase 7: User Story 5 - Delete Todo Items (Priority: P2)

Goal: Enable users to remove tasks from their list when they no longer need them

Independent Test: User can delete a todo and verify it no longer appears in the list, delivering the value of task removal.

**Acceptance**:
1. Given a list with multiple todos, when user deletes a specific todo, then that todo is removed from the list and no longer appears when viewing

- [X] T046 [P] [US5] Implement delete_todo method in InMemoryTodoRepository
- [X] T047 [US5] Implement delete_todo method in TodoService
- [X] T048 [US5] Implement delete todo command in cli.py
- [X] T049 [US5] Display menu with "Delete Todo" option
- [X] T050 [P] [US5] Create unit tests for repository delete functionality
- [X] T051 [P] [US5] Create unit tests for TodoService delete functionality
- [X] T052 [US5] Create integration tests for delete todo flow

## Phase 8: Polish & Cross-Cutting Concerns

Goal: Implement error handling, validation, and finalize the application

- [X] T053 [P] Implement comprehensive input validation in cli.py
- [X] T054 [P] Add error handling for invalid todo IDs in all operations
- [X] T055 [P] Handle edge case: marking non-existent todo as complete
- [X] T056 [P] Handle edge case: updating/deleting non-existent todos
- [X] T057 [P] Handle edge case: empty or whitespace-only todo descriptions
- [X] T058 [P] Handle edge case: very long todo descriptions (1000 char limit)
- [X] T059 [P] Add user-friendly error messages for all operations
- [X] T060 [P] Implement graceful exit functionality
- [X] T061 [P] Add comprehensive logging/error reporting
- [X] T062 [P] Create additional integration tests for edge cases
- [X] T063 [P] Add type hints throughout the codebase
- [X] T064 [P] Add docstrings to all public methods and classes
- [X] T065 [P] Perform final code review and cleanup
- [X] T066 [P] Verify all functional requirements from spec are met
- [X] T067 [P] Create final README with usage instructions
- [X] T068 [P] Run full test suite to ensure all functionality works