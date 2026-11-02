# 06 - Lists and Tuples

Run it: `python lists_tuples.py`

## Lists
An ordered, **mutable** collection: `[1, "two", 3.0]`.

### Adding and removing
| Method | Effect |
|--------|--------|
| `append(x)` | add to the end |
| `insert(i, x)` | add at position `i` |
| `extend(iterable)` | add many items |
| `remove(x)` | delete first matching value |
| `pop(i)` | remove and return item (last by default) |
| `del lst[i]` | delete by index |
| `clear()` | empty the list |

### Searching and sorting
`index()`, `count()`, `in`, `min()`, `max()`, `sum()`. `sort()` changes the list in place; `sorted()` returns a new one. Both accept `key=` and `reverse=`.

### Copy trap
`b = a` makes both names point to the **same** list. Use `a.copy()` or `a[:]` for a real copy. For nested lists use `copy.deepcopy`.

### List comprehensions
`[expr for item in iterable if condition]` builds a list in one line. Example: `[x**2 for x in range(5)]`.

### Nested lists
A list of lists represents a matrix: `matrix[row][col]`.

### Stack and queue
A list works as a stack (`append` + `pop`). For a queue use `collections.deque`, which is fast at both ends.

## Tuples
An ordered, **immutable** collection: `(4, 7)`. A single-item tuple needs a comma: `(5,)`.

- Faster and safer than lists when data should not change
- Support unpacking: `x, y = point`, `first, *rest = items`
- Hashable (if their contents are), so they can be dictionary keys or set members

## Practice
1. Find the second largest number in a list.
2. Remove duplicates while keeping order.
3. Rotate a list by `k` positions.
