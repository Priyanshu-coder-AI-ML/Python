# 03 - Loops

Run it: `python loops.py`

## What you learn

### for loop
Repeats once for each item in a sequence (list, string, range, dict, ...).

### range()
- `range(5)` gives 0,1,2,3,4
- `range(1, 11, 2)` gives 1,3,5,7,9 (start, stop, step; stop is excluded)
- `range(5, 0, -1)` counts down

### Handy helpers
- `enumerate(seq, start=1)` gives index and value together
- `zip(a, b)` walks two sequences in parallel

### while loop
Repeats as long as a condition is true. Make sure something inside the loop changes the condition, otherwise it runs forever.

### break, continue, else
- `break` exits the loop immediately
- `continue` skips to the next iteration
- `for ... else` / `while ... else`: the `else` block runs only if the loop finished without `break`

### Nested loops
A loop inside a loop. Used for tables, grids and patterns. The inner loop runs fully for each pass of the outer loop.

### Classic programs included
Sum of numbers, factorial, Fibonacci series, prime check, star patterns.

## Practice
1. Print the multiplication table of any number.
2. Count vowels in a string.
3. Print a number pyramid.
