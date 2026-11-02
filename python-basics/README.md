# Python Basics - Code and Guides

A complete set of runnable Python examples, one folder per topic. Each folder has a `.py` file full of commented examples and a `README.md` that explains the concepts.

## Requirements
Python 3.10 or newer (the `match` statement in topic 2 needs 3.10+). Check with `python --version`.

## How to use
```bash
cd python-basics/01_variables_and_data_types
python variables.py
```
Read the README first, run the script, then edit the code and experiment. Finish the **Practice** exercises at the end of each README before moving on.

## Topics

| # | Folder | What it covers |
|---|--------|----------------|
| 01 | `01_variables_and_data_types` | variables, data types, casting, operators, input/output |
| 02 | `02_conditionals` | `if` / `elif` / `else`, ternary, `match` |
| 03 | `03_loops` | `for`, `while`, `range`, `break`, `continue`, nested loops, patterns |
| 04 | `04_functions` | parameters, return values, `*args`, `**kwargs`, scope, lambda, recursion |
| 05 | `05_strings` | slicing, methods, f-strings, formatting, string programs |
| 06 | `06_lists_and_tuples` | list methods, sorting, comprehensions, matrices, tuples |
| 07 | `07_dictionaries_and_sets` | dict operations, `Counter`, `defaultdict`, set maths |
| 08 | `08_file_handling` | text, CSV, JSON, `pathlib` |
| 09 | `09_exceptions` | `try` / `except` / `else` / `finally`, `raise`, custom errors |
| 10 | `10_oop` | classes, inheritance, polymorphism, dunder methods, dataclasses |
| 11 | `11_modules_and_comprehensions` | imports, generators, iterators, context managers, `venv` |
| 12 | `12_mini_projects` | seven small projects combining everything |

## Suggested order
Follow the numbers. Topics 1-4 are the foundation, 5-7 cover Python's data structures, 8-9 make programs robust, 10-11 are intermediate tools, and 12 puts it all together.

## Tips
- Type the code yourself instead of only reading it
- Change values and predict the output before running
- Use `help(function_name)` or `dir(object)` in the Python shell to explore
- Read error messages from the bottom up; the last line names the problem
