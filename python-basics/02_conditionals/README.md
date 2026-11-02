# 02 - Conditional Statements

Run it: `python conditionals.py`

## What you learn

### if / elif / else
Python picks the first condition that is true and skips the rest. Indentation (4 spaces) defines the block.

```python
if marks >= 75:
    ...
elif marks >= 60:
    ...
else:
    ...
```

### Nested conditions
An `if` can live inside another `if`. Keep nesting shallow; combine conditions with `and` / `or` when it stays readable.

### Truthy and falsy
These count as `False`: `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`, `None`. Everything else is `True`. So `if items:` means "if the list is not empty".

### Useful operators in conditions
- `in` / `not in` - membership (`"e" in "hello"`)
- `is` / `is not` - identity, mainly for `None`
- Chained comparison - `40 <= score <= 60`

### Ternary expression
`value_if_true if condition else value_if_false` fits a simple choice on one line.

### match / case
Available from Python 3.10. Similar to `switch` in other languages. `_` is the default case and `|` combines several patterns.

## Practice
1. Check whether a number is positive, negative or zero.
2. Build a simple grade calculator.
3. Find the largest of three numbers.
