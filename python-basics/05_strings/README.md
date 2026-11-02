# 05 - Strings

Run it: `python strings.py`

## What you learn

### Indexing and slicing
- `s[0]` first character, `s[-1]` last character
- `s[start:stop:step]` - stop is excluded
- `s[::-1]` reverses a string

### Immutability
Strings cannot be changed in place. Methods return a **new** string, so assign the result: `s = s.strip()`.

### Frequently used methods
| Method | Purpose |
|--------|---------|
| `strip()` | remove surrounding whitespace |
| `lower()` / `upper()` / `title()` | change case |
| `replace(old, new)` | substitute text |
| `split(sep)` | string to list |
| `sep.join(list)` | list to string |
| `find()` / `index()` | locate a substring |
| `count()` | count occurrences |
| `startswith()` / `endswith()` | prefix and suffix tests |
| `isdigit()`, `isalpha()`, `isalnum()` | content checks |

### Formatting
f-strings are preferred: `f"{score:.2f}"`. Format specs control decimals, alignment (`<`, `>`, `^`), thousands separators (`,`) and percentages (`%`).

### Escapes and raw strings
`\n` newline, `\t` tab, `\"` quote. A raw string `r"..."` keeps backslashes literally (useful for file paths and regex).

### Multiline strings
Triple quotes `""" ... """` keep line breaks.

### Programs included
Palindrome check, vowel counter, title-casing a sentence, character frequency.

## Practice
1. Count the words in a sentence.
2. Check whether two strings are anagrams.
3. Remove all spaces and punctuation from a string.
