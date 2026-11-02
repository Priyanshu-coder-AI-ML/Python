"""Topic 6: Lists and tuples."""

# ================= LISTS =================
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]

print("--- access ---")
print(fruits[0], fruits[-1])
print(fruits[1:])
print(len(fruits))

# ---------- Modifying ----------
print("\n--- modify ---")
fruits[1] = "blueberry"             # lists are mutable
fruits.append("date")               # add to end
fruits.insert(1, "avocado")         # add at position
fruits.extend(["fig", "grape"])     # add many
print(fruits)

fruits.remove("fig")                # remove by value
last = fruits.pop()                 # remove and return last
del fruits[0]                       # remove by index
print(fruits, "| popped:", last)

# ---------- Searching and counting ----------
nums = [5, 3, 8, 3, 1, 9, 3]
print("\n--- search ---")
print(nums.index(8))
print(nums.count(3))
print(8 in nums)
print(min(nums), max(nums), sum(nums))

# ---------- Sorting ----------
print("\n--- sort ---")
nums.sort()                         # in place
print(nums)
nums.sort(reverse=True)
print(nums)
print(sorted(["pear", "fig", "apple"], key=len))   # returns new list
nums.reverse()
print(nums)

# ---------- Copying (common trap) ----------
print("\n--- copying ---")
a = [1, 2, 3]
b = a                               # same list, not a copy
c = a.copy()                        # real copy
a.append(4)
print("a:", a, "b:", b, "c:", c)

# ---------- List comprehensions ----------
print("\n--- comprehensions ---")
squares = [x ** 2 for x in range(1, 8)]
evens = [x for x in range(20) if x % 2 == 0]
words = ["hi", "python", "go"]
lengths = [len(w) for w in words]
print(squares)
print(evens)
print(lengths)

# ---------- Nested lists (matrix) ----------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n--- matrix ---")
for row in matrix:
    print(row)
print("center:", matrix[1][1])
print("transpose:", [list(r) for r in zip(*matrix)])

# ---------- Stack and queue ----------
stack = []
stack.append(1)
stack.append(2)
print("\nstack pop:", stack.pop())    # LIFO

from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print("queue pop:", queue.popleft())  # FIFO

# ================= TUPLES =================
print("\n--- tuples ---")
point = (4, 7)
single = (5,)                       # comma makes it a tuple
print(point[0], point[1])
# point[0] = 1                      # TypeError: immutable

x, y = point                        # unpacking
print(x, y)

first, *rest = (1, 2, 3, 4)
print(first, rest)

print(point + (1, 2))
print((1, 2) * 3)
print(point.count(4), point.index(7))

# Tuples can be dict keys because they are hashable
locations = {(0, 0): "origin", (1, 2): "point A"}
print(locations[(1, 2)])
