# 04 - Functions

Run it: `python functions.py`

## What you learn

### Defining and calling
```python
def greet(name):
    return f"Hello, {name}"
```
Define with `def`, call with parentheses. The first string inside is the **docstring**.

### Return values
`return` sends a value back and ends the function. Returning several values gives a tuple, which you can unpack: `low, high = min_max(nums)`. A function with no `return` gives `None`.

### Parameters
- **Default values**: `def power(base, exponent=2)`
- **Keyword arguments**: `power(exponent=3, base=4)`
- **`*args`**: collects extra positional arguments into a tuple
- **`**kwargs`**: collects extra keyword arguments into a dict

Never use a mutable default such as `def f(x=[])`; use `None` and create the list inside.

### Scope (LEGB)
Python looks up names in this order: Local, Enclosing, Global, Built-in. Use `global` to modify a global variable (use sparingly).

### Lambda
A small anonymous function: `lambda x: x * x`. Common with `sorted`, `map` and `filter`.

### Recursion
A function calling itself. Always needs a **base case**, otherwise it never stops.

### Type hints
`def area(w: float, h: float) -> float` documents expected types. Python does not enforce them, but tools and editors use them.

### Decorators (preview)
A function that wraps another function to add behavior. Shown briefly at the end of the file.

## Practice
1. Write a function that checks whether a number is prime.
2. Write a function that reverses a string.
3. Write a calculator with one function per operation.
