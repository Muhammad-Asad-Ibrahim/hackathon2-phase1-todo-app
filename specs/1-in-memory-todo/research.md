# Research: In-Memory Python Console Todo App (Phase I)

**Feature**: 1-in-memory-todo
**Date**: 2026-01-09

## Overview

This research document captures technical decisions and best practices for implementing the in-memory Python console todo application. It addresses all technical unknowns and clarifies implementation approaches.

## Architecture Decision: Layered Structure

**Decision**: Implement a three-layer architecture (Domain, Application, Interface) as specified in the requirements.

**Rationale**: This follows the separation of concerns principle from the constitution and provides clear boundaries between business logic, application operations, and user interface. This approach makes the code more maintainable and testable.

**Alternatives considered**:
- Monolithic structure: Would mix concerns and reduce maintainability
- MVC pattern: Not ideal for console applications
- Functional approach: Would make state management harder

## Technology Choice: Python 3.13+

**Decision**: Use Python 3.13+ with standard library only (no external dependencies).

**Rationale**:
- Aligns with feature requirements
- Provides modern syntax and performance improvements
- Standard library is sufficient for console application
- No need for external packages that would violate the no-dependencies constraint

**Alternatives considered**:
- Earlier Python versions: Would lack newer features and optimizations
- Additional libraries: Would violate the no-external-dependencies constraint

## Data Model: Todo Entity

**Decision**: Create a Todo class with id, title, and completion status fields.

**Rationale**:
- Matches the specification requirements
- Simple structure that supports all required operations
- Easy to serialize/deserialize if needed in future phases

**Fields**:
- `id`: Unique identifier (UUID or auto-incrementing integer)
- `title`: String representing the task description
- `completed`: Boolean indicating completion status

## In-Memory Storage Approach

**Decision**: Use Python dictionary for storage with UUID keys or auto-incrementing integer IDs.

**Rationale**:
- Provides O(1) lookup performance
- Simple implementation with standard library
-符合 the in-memory-only requirement
- Easy to iterate over for listing operations

**Alternatives considered**:
- List-based storage: Less efficient for update/delete operations
- Custom data structure: Unnecessary complexity for this phase

## Console Interface Design

**Decision**: Implement a menu-driven command loop with numbered options.

**Rationale**:
- Familiar pattern for console applications
- Easy to implement and test
- Clear user interaction flow
-符合 the console-only requirement

**Menu options**:
1. Add todo
2. View todos
3. Update todo
4. Delete todo
5. Mark todo as complete/incomplete
6. Exit

## Error Handling Strategy

**Decision**: Use try-except blocks with user-friendly error messages.

**Rationale**:
- Provides clear feedback to users
- Prevents application crashes
-符合 the error handling requirements in the spec
- Makes the application robust against invalid inputs

## Testing Approach

**Decision**: Use pytest for unit and integration testing.

**Rationale**:
- Most popular Python testing framework
- Good integration with VS Code and other editors
- Supports parametrized tests
-符合 the testing requirements

## Validation and Input Sanitization

**Decision**: Implement input validation at the interface layer.

**Rationale**:
- Prevents invalid data from entering the system
- Provides immediate feedback to users
-符合 the validation requirements in the spec
- Improves user experience

**Validation rules**:
- Todo titles must not be empty or only whitespace
- IDs must exist when performing update/delete operations
- Menu selections must be valid options