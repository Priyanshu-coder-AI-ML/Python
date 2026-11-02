# 09 - Exception Handling

Run it: `python exceptions.py`

## What you learn

### Why exceptions
Errors at run time (bad input, missing file, divide by zero) stop the program unless you handle them.

### Structure
```python
try:
    risky_code()
except SomeError as e:
    handle(e)
else:
    runs_if_no_error()
finally:
    always_runs()
```

| Block | When it runs |
|-------|--------------|
| `try` | the code that might fail |
| `except` | when a matching error occurs |
| `else` | only if no error occurred |
| `finally` | always; ideal for cleanup |

### Catching well
- Catch **specific** exceptions; avoid a bare `except:`
- Group several: `except (TypeError, KeyError):`
- Use `as e` to read the error message

### Raising exceptions
`raise ValueError("message")` signals a problem yourself, for example when validating input.

### Custom exceptions
Subclass `Exception` to create meaningful error types such as `InsufficientFundsError`.

### Chaining
`raise NewError(...) from original` keeps the original cause visible while adding context.

### assert
`assert condition, "message"` is a quick sanity check for developers, not for validating user input.

### Common built-in exceptions
`ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`, `AttributeError`, `NameError`, `ImportError`.

## Practice
1. Read a number from the user and keep asking until it is valid.
2. Safely read a file and report if it does not exist.
3. Create a custom exception for an invalid password.
