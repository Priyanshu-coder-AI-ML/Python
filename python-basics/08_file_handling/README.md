# 08 - File Handling

Run it: `python file_handling.py`

The script creates a temporary `sample_files/` folder, uses it, and deletes it at the end.

## What you learn

### Opening files
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    data = f.read()
```
Always use `with`; it closes the file automatically, even if an error occurs.

### Modes
| Mode | Meaning |
|------|---------|
| `r` | read (default); error if file is missing |
| `w` | write; **erases** existing content |
| `a` | append to the end |
| `x` | create; error if it already exists |
| `b` | add for binary files, e.g. `rb` |

### Reading
- `f.read()` whole file as one string
- `f.readline()` one line
- `f.readlines()` list of lines
- `for line in f:` best for large files (reads lazily)

### Writing
`f.write(text)` and `f.writelines(list)`. Neither adds newlines for you.

### CSV
The `csv` module handles commas and quotes correctly. Use `csv.reader` / `csv.writer` for lists and `csv.DictReader` for rows as dictionaries. Open with `newline=""`.

### JSON
`json.dump` / `json.load` work with files; `json.dumps` / `json.loads` work with strings. Great for saving settings and structured data.

### pathlib
`Path` objects make paths portable across operating systems: `exists()`, `name`, `suffix`, `glob()`, `read_text()`, `write_text()`, `mkdir()`, `unlink()`.

### Handling errors
Wrap risky file operations in `try / except FileNotFoundError`.

## Practice
1. Copy the contents of one file into another.
2. Count lines, words and characters in a file.
3. Store a to-do list in a JSON file and read it back.
