"""Topic 2: Conditional statements (if / elif / else, match)."""

# ---------- Simple if / elif / else ----------
marks = 76

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Marks: {marks} -> Grade: {grade}")

# ---------- Nested if ----------
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID")
else:
    print("Too young")

# ---------- Combining conditions ----------
temperature = 28
is_raining = False

if temperature > 25 and not is_raining:
    print("Great day for cricket")
elif is_raining:
    print("Stay inside")
else:
    print("Take a jacket")

# ---------- Truthy / falsy checks ----------
items = []
if items:
    print("List has items")
else:
    print("List is empty")

# ---------- Membership and identity ----------
vowels = "aeiou"
letter = "e"
if letter in vowels:
    print(f"{letter} is a vowel")

value = None
if value is None:
    print("value is None")

# ---------- Ternary (conditional expression) ----------
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"{number} is {parity}")

# ---------- Chained comparison ----------
score = 55
if 40 <= score <= 60:
    print("Score is between 40 and 60")

# ---------- match / case (Python 3.10+) ----------
command = "stop"

match command:
    case "start":
        print("Starting...")
    case "stop" | "halt":
        print("Stopping...")
    case _:
        print("Unknown command")

# ---------- Example: leap year ----------
year = 2028
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
