"""Topic 8: File handling (text, CSV, JSON, pathlib)."""

import csv
import json
from pathlib import Path

# Work inside a folder next to this script so nothing else is touched
BASE = Path(__file__).parent / "sample_files"
BASE.mkdir(exist_ok=True)

# ---------- Writing a text file ----------
notes = BASE / "notes.txt"
with open(notes, "w", encoding="utf-8") as f:     # "w" overwrites
    f.write("Line one\n")
    f.write("Line two\n")
    f.writelines(["Line three\n", "Line four\n"])

# ---------- Appending ----------
with open(notes, "a", encoding="utf-8") as f:     # "a" adds to the end
    f.write("Line five\n")

# ---------- Reading ----------
print("--- read whole file ---")
with open(notes, "r", encoding="utf-8") as f:
    print(f.read())

print("--- read line by line ---")
with open(notes, encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.rstrip())

print("--- readlines ---")
with open(notes, encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines), "lines")

# ---------- Word count example ----------
with open(notes, encoding="utf-8") as f:
    words = f.read().split()
print("words:", len(words))

# ---------- CSV ----------
people = BASE / "people.csv"
rows = [
    ["name", "age", "city"],
    ["Asha", 19, "Pune"],
    ["Ravi", 20, "Surat"],
]
with open(people, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

print("\n--- csv reader ---")
with open(people, newline="", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)

print("--- csv DictReader ---")
with open(people, newline="", encoding="utf-8") as f:
    for record in csv.DictReader(f):
        print(record["name"], record["city"])

# ---------- JSON ----------
config = {"user": "Zorshu", "skills": ["python", "ml"], "active": True}
config_file = BASE / "config.json"
with open(config_file, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

with open(config_file, encoding="utf-8") as f:
    loaded = json.load(f)
print("\njson loaded:", loaded)
print(json.dumps(loaded))                          # object -> string

# ---------- pathlib ----------
print("\n--- pathlib ---")
print("exists:", notes.exists())
print("name:", notes.name, "| suffix:", notes.suffix, "| stem:", notes.stem)
print("size:", notes.stat().st_size, "bytes")
print("text files:", sorted(p.name for p in BASE.glob("*.txt")))
print(notes.read_text(encoding="utf-8").splitlines()[0])

# ---------- Safe handling of a missing file ----------
try:
    with open(BASE / "missing.txt") as f:
        f.read()
except FileNotFoundError:
    print("\nmissing.txt does not exist")

# ---------- Cleanup ----------
for p in BASE.iterdir():
    p.unlink()
BASE.rmdir()
print("cleaned up")
