"""Topic 7: Dictionaries and sets."""

# ================= DICTIONARIES =================
student = {"name": "Zorshu", "course": "AIML", "year": 1}

print("--- access ---")
print(student["name"])
print(student.get("city", "Unknown"))   # safe access with default
print(student.keys())
print(student.values())
print(student.items())

# ---------- Modifying ----------
print("\n--- modify ---")
student["year"] = 2                     # update
student["city"] = "Vadodara"            # add
student.update({"semester": 3, "year": 1})
removed = student.pop("city")           # remove and return
print(student, "| removed:", removed)
student.setdefault("grade", "A")        # add only if missing
print(student)

# ---------- Looping ----------
print("\n--- looping ---")
for key, value in student.items():
    print(f"{key} -> {value}")

# ---------- Membership ----------
print("name" in student)                # checks keys
print("Zorshu" in student.values())

# ---------- Dictionary comprehension ----------
squares = {n: n ** 2 for n in range(1, 6)}
print("\nsquares:", squares)

# ---------- Counting and grouping ----------
print("\n--- counting ---")
text = "to be or not to be"
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
print(count)

from collections import Counter, defaultdict
print(Counter(text.split()).most_common(2))

groups = defaultdict(list)
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    groups[word[0]].append(word)
print(dict(groups))

# ---------- Nested dictionary ----------
school = {
    "A101": {"name": "Asha", "marks": 88},
    "A102": {"name": "Ravi", "marks": 92},
}
print("\n", school["A102"]["name"])
for roll, info in school.items():
    print(roll, info["name"], info["marks"])

# ---------- Sorting a dictionary ----------
marks = {"Asha": 88, "Ravi": 92, "Meera": 79}
by_marks = dict(sorted(marks.items(), key=lambda kv: kv[1], reverse=True))
print("\nsorted:", by_marks)

# ---------- Merging (Python 3.9+) ----------
d1, d2 = {"a": 1, "b": 2}, {"b": 3, "c": 4}
print(d1 | d2)                          # right side wins on clashes

# ================= SETS =================
print("\n--- sets ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
empty = set()                           # {} would create a dict

a.add(10)
a.discard(10)                           # no error if missing
print(a)

print("union:        ", a | b)
print("intersection: ", a & b)
print("difference:   ", a - b)
print("symmetric diff:", a ^ b)
print("subset:", {1, 2} <= a)

# Removing duplicates
data = [1, 2, 2, 3, 3, 3, 4]
print(list(set(data)))
print(list(dict.fromkeys(data)))        # removes duplicates, keeps order

# Set comprehension
print({c for c in "programming" if c not in "aeiou"})

# Fast membership testing
big = set(range(100000))
print(99999 in big)
