# 01 - Variables, Data Types, Input/Output and Operators

Run it: `python variables.py`

## What you learn

### Variables
A variable is a name that points to a value. Python needs no type declaration; the type comes from the value.

```python
age = 18
```

Naming rules: letters, digits and `_` only, cannot start with a digit, case-sensitive, and cannot be a keyword such as `if` or `for`. Use `snake_case` by convention.

### Core data types
| Type | Example | Notes |
|------|---------|-------|
| `int` | `42` | whole numbers, unlimited size |
| `float` | `3.14` | decimal numbers |
| `str` | `"hello"` | text |
| `bool` | `True` / `False` | used in conditions |
| `NoneType` | `None` | "no value" |
| `complex` | `3 + 4j` | rarely needed early on |

Use `type(x)` to check a type.

### Type conversion
`int()`, `float()`, `str()`, `bool()` convert between types. `int(7.9)` gives `7` because it truncates. Falsy values (`0`, `""`, `[]`, `None`) convert to `False`; everything else is `True`.

### Operators
- Arithmetic: `+ - * / // % **`
- Comparison: `== != > < >= <=`
- Logical: `and or not`
- Assignment: `= += -= *= /=`

`/` always returns a float. `//` is floor division. `%` is the remainder.

### Input and output
- `print()` shows output. `sep` and `end` control separators and line endings.
- `input()` always returns a **string**, so convert it with `int()` or `float()` when you need a number.
- f-strings (`f"{name}"`) are the modern way to format text.

## Practice
1. Ask for two numbers and print their sum, difference and product.
2. Convert a temperature from Celsius to Fahrenheit.
3. Swap two variables without a third one.
