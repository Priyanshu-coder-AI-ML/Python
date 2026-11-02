# 12 - Mini Projects

Run it: `python mini_projects.py`

These projects combine the earlier topics so you can see how the pieces fit together.

| # | Project | Topics used |
|---|---------|-------------|
| 1 | Calculator | functions, dicts of lambdas, exceptions |
| 2 | Number guessing game | loops, conditionals, `enumerate` |
| 3 | Password strength checker | strings, `any()`, booleans as numbers |
| 4 | To-do list saved to JSON | classes, file handling, JSON, `pathlib` |
| 5 | Grade book | dictionaries, loops, ternary, `max(key=)` |
| 6 | Word frequency counter | strings, dictionaries, sorting |
| 7 | Bank account | OOP, exceptions, tuples |

## How to use them
The demo at the bottom of the file runs with fixed values so it works instantly. To make a project interactive, replace the demo values with `input()` calls and wrap the conversion in `try / except ValueError`.

## Challenges to extend them
1. Calculator: add `**` and `%`, and keep a history of results.
2. Guessing game: let the player choose a difficulty and count score across rounds.
3. To-do list: add delete and edit, and show only unfinished tasks.
4. Grade book: read marks from a CSV file and export the report to JSON.
5. Bank account: add a `transfer()` method between two accounts.
6. Combine ideas into a command-line menu using a `while True` loop.

## Where to go next
- Libraries: `requests` (web APIs), `pandas` and `numpy` (data), `matplotlib` (charts)
- Testing: `pytest`
- Machine learning: `scikit-learn`, then `PyTorch` or `TensorFlow`
