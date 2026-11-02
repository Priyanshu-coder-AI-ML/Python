"""Topic 12: Mini projects that combine everything learned.

Run with:  python mini_projects.py
Each project is a function; the demo at the bottom uses fixed inputs so the
script runs without waiting for typing. Replace the demo values with input()
when you want to use them interactively.
"""

import json
import random
from pathlib import Path


# ---------- Project 1: Simple calculator ----------
def calculate(a, op, b):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if op not in operations:
        raise ValueError(f"Unknown operator: {op}")
    try:
        return operations[op](a, b)
    except ZeroDivisionError:
        return "Cannot divide by zero"


# ---------- Project 2: Number guessing game ----------
def guessing_game(secret, guesses):
    for attempt, guess in enumerate(guesses, start=1):
        if guess == secret:
            return f"Correct in {attempt} tries!"
        hint = "higher" if guess < secret else "lower"
        print(f"  Guess {guess}: try {hint}")
    return f"Out of guesses. The number was {secret}"


# ---------- Project 3: Password strength checker ----------
def check_password(pw):
    score = 0
    score += len(pw) >= 8
    score += any(c.islower() for c in pw)
    score += any(c.isupper() for c in pw)
    score += any(c.isdigit() for c in pw)
    score += any(not c.isalnum() for c in pw)
    return ["Very weak", "Weak", "Fair", "Good", "Strong", "Excellent"][score]


# ---------- Project 4: To-do list saved to JSON ----------
class TodoList:
    def __init__(self, path):
        self.path = Path(path)
        self.tasks = json.loads(self.path.read_text()) if self.path.exists() else []

    def add(self, title):
        self.tasks.append({"title": title, "done": False})
        self._save()

    def complete(self, index):
        self.tasks[index]["done"] = True
        self._save()

    def show(self):
        for i, t in enumerate(self.tasks):
            mark = "x" if t["done"] else " "
            print(f"  [{mark}] {i}: {t['title']}")

    def _save(self):
        self.path.write_text(json.dumps(self.tasks, indent=2))


# ---------- Project 5: Student grade book ----------
def grade_report(students):
    report = {}
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 50 else "F"
        report[name] = (round(avg, 1), grade)
    best = max(report, key=lambda n: report[n][0])
    return report, best


# ---------- Project 6: Word frequency counter ----------
def top_words(text, n=3):
    cleaned = "".join(c.lower() if c.isalnum() or c.isspace() else " " for c in text)
    freq = {}
    for word in cleaned.split():
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


# ---------- Project 7: Simple bank account (OOP) ----------
class Account:
    def __init__(self, owner, balance=0):
        self.owner, self.balance, self.history = owner, balance, []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))


# ---------- Demo ----------
if __name__ == "__main__":
    print("1. Calculator")
    print("  12 * 7 =", calculate(12, "*", 7))
    print("  5 / 0  =", calculate(5, "/", 0))

    print("\n2. Guessing game")
    random.seed(1)
    secret = random.randint(1, 20)
    print(" ", guessing_game(secret, [10, 15, 5, secret]))

    print("\n3. Password strength")
    for pw in ("abc", "Python123", "Tr0ub4dor&3"):
        print(f"  {pw!r}: {check_password(pw)}")

    print("\n4. To-do list")
    todo_path = Path(__file__).parent / "_demo_todo.json"
    todo = TodoList(todo_path)
    todo.add("Finish Python basics")
    todo.add("Start the startup prototype")
    todo.complete(0)
    todo.show()
    todo_path.unlink()                       # clean up demo file

    print("\n5. Grade book")
    report, best = grade_report({"Asha": [88, 92, 79], "Ravi": [60, 72, 65], "Meera": [95, 91, 98]})
    for name, (avg, grade) in report.items():
        print(f"  {name}: {avg} -> {grade}")
    print("  Top student:", best)

    print("\n6. Top words")
    print(" ", top_words("the cat and the hat and the bat"))

    print("\n7. Bank account")
    acct = Account("Zorshu", 1000)
    acct.deposit(250)
    acct.withdraw(100)
    print(f"  {acct.owner}: {acct.balance}", acct.history)
