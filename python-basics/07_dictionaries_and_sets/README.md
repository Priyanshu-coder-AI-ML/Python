# 07 - Dictionaries and Sets

Run it: `python dicts_sets.py`

## Dictionaries
Store **key: value** pairs. Keys must be unique and hashable (strings, numbers, tuples). Since Python 3.7 they keep insertion order.

### Core operations
| Operation | Example |
|-----------|---------|
| create | `d = {"a": 1}` |
| read | `d["a"]` (error if missing) or `d.get("a", default)` |
| add / update | `d["b"] = 2`, `d.update({...})` |
| remove | `d.pop("a")`, `del d["a"]` |
| views | `d.keys()`, `d.values()`, `d.items()` |
| default insert | `d.setdefault("k", v)` |
| merge | `d1 | d2` (3.9+) |

### Looping
`for key, value in d.items():` is the standard pattern.

### Useful tools
- **Dict comprehension**: `{n: n**2 for n in range(5)}`
- **`Counter`**: counts items quickly
- **`defaultdict`**: creates missing entries automatically
- **Nested dictionaries**: model records like `school["A101"]["name"]`
- **Sorting**: `sorted(d.items(), key=...)`

## Sets
An unordered collection of **unique** items.

- Create with `{1, 2, 3}`; use `set()` for an empty set (`{}` is an empty dict)
- `add()`, `discard()`, `remove()`, `pop()`
- Math operations: union `|`, intersection `&`, difference `-`, symmetric difference `^`
- Very fast membership tests (`x in my_set`)
- Common use: removing duplicates

## When to use what
| Need | Use |
|------|-----|
| ordered, changeable | list |
| ordered, fixed | tuple |
| lookup by key | dict |
| unique items, set maths | set |

## Practice
1. Count word frequency in a paragraph.
2. Find common elements of two lists using sets.
3. Build a phone book with add, search and delete.
