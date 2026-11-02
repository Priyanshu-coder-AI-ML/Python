"""Topic 11: Modules, comprehensions, generators, iterators and context managers."""

# ---------- Importing modules ----------
import math
import random
import datetime as dt
from collections import Counter
from itertools import combinations, permutations

print("--- standard library ---")
print(math.sqrt(144), math.pi, math.ceil(4.2), math.floor(4.8))
print(math.gcd(12, 18), math.factorial(5))

random.seed(42)                              # makes results repeatable
print(random.randint(1, 10), random.choice(["a", "b", "c"]))
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)

today = dt.date(2026, 11, 2)
print(today.strftime("%d %B %Y"), "|", today.weekday())
print(today + dt.timedelta(days=30))

print(Counter("hello world").most_common(2))
print(list(combinations("ABC", 2)))
print(len(list(permutations("ABC"))))

# ---------- Creating your own module ----------
# Any .py file is a module. If you save the following as mytools.py:
#
#     def square(x): return x * x
#     if __name__ == "__main__":
#         print("run directly")
#
# you can use it anywhere with:  from mytools import square
#
# The __name__ check lets a file work both as a script and as an import.

# ---------- Comprehensions ----------
print("\n--- comprehensions ---")
print([x * x for x in range(6)])
print([x for x in range(20) if x % 3 == 0])
print({w: len(w) for w in ["python", "is", "fun"]})
print({n % 3 for n in range(10)})
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)
print(["even" if n % 2 == 0 else "odd" for n in range(4)])

# ---------- Generators ----------
print("\n--- generators ---")


def countdown(n):
    while n > 0:
        yield n                              # pauses here, resumes later
        n -= 1


print(list(countdown(5)))

gen = (x ** 2 for x in range(1_000_000))     # generator expression, no big list
print(next(gen), next(gen), next(gen))
print(sum(x for x in range(101)))


def fib():
    a, b = 0, 1
    while True:                              # infinite generator
        yield a
        a, b = b, a + b


from itertools import islice
print(list(islice(fib(), 10)))

# ---------- Iterators ----------
print("\n--- iterators ---")
it = iter([10, 20, 30])
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("iterator exhausted")


class Repeater:
    def __init__(self, value, times):
        self.value, self.times = value, times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times <= 0:
            raise StopIteration
        self.times -= 1
        return self.value


print(list(Repeater("hi", 3)))

# ---------- Useful built-ins ----------
print("\n--- built-ins ---")
nums = [4, 1, 7, 3]
print(any(n > 6 for n in nums), all(n > 0 for n in nums))
print(sorted(nums), list(reversed(nums)))
print(list(map(str, nums)), list(zip("abc", nums)))
print(max(nums, key=lambda n: -n))

# ---------- Context managers ----------
print("\n--- context managers ---")
from contextlib import contextmanager


@contextmanager
def section(title):
    print(f"[start {title}]")
    try:
        yield
    finally:
        print(f"[end {title}]")


with section("demo"):
    print("inside the block")

# ---------- Timing code ----------
import time
start = time.perf_counter()
sum(range(1_000_000))
print(f"\nTook {time.perf_counter() - start:.4f} seconds")

# ---------- Virtual environments and pip (run in a terminal) ----------
#   python -m venv .venv
#   source .venv/bin/activate        (Windows: .venv\Scripts\activate)
#   pip install requests
#   pip freeze > requirements.txt
