# 11 - Modules, Comprehensions, Generators and More

Run it: `python modules_and_more.py`

## What you learn

### Modules and imports
A module is any `.py` file. Import styles:

```python
import math                      # math.sqrt(9)
import datetime as dt            # alias
from collections import Counter  # specific name
```
Useful standard-library modules: `math`, `random`, `datetime`, `collections`, `itertools`, `json`, `os`, `pathlib`, `time`, `re`.

**`if __name__ == "__main__":`** lets a file run as a script but not execute that code when imported.

### Comprehensions
Compact ways to build collections:
- list `[x*x for x in range(5)]`
- dict `{w: len(w) for w in words}`
- set `{n % 3 for n in range(10)}`
- with a filter `[x for x in data if x > 0]`

Keep them short; use a normal loop if one becomes hard to read.

### Generators
Functions that use `yield` produce values one at a time and remember their place. They use very little memory, and can even be infinite. A generator expression looks like a list comprehension with `()`.

### Iterators
An object is an iterator if it has `__iter__` and `__next__`. `iter()` and `next()` drive it, and `StopIteration` signals the end. This is what `for` loops use behind the scenes.

### Built-in helpers
`any`, `all`, `sorted`, `reversed`, `map`, `zip`, `enumerate`, `min`/`max` with `key=`.

### Context managers
The `with` statement guarantees setup and cleanup. Create your own with `@contextmanager` or by defining `__enter__` / `__exit__`.

### Virtual environments and pip
Keep each project's packages separate:
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install requests
pip freeze > requirements.txt
```

## Practice
1. Write a generator that yields prime numbers.
2. Create your own module with three helper functions and import it.
3. Roll two dice 1000 times with `random` and count each total.
