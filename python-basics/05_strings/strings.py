"""Topic 5: Strings."""

text = "Python Programming"

# ---------- Indexing and slicing ----------
print("--- indexing & slicing ---")
print(text[0])          # first character
print(text[-1])         # last character
print(text[0:6])        # 'Python'
print(text[7:])         # 'Programming'
print(text[:6])
print(text[::2])        # every 2nd character
print(text[::-1])       # reversed
print(len(text))

# ---------- Strings are immutable ----------
# text[0] = "J"         # TypeError
new_text = "J" + text[1:]
print(new_text)

# ---------- Common methods ----------
print("\n--- methods ---")
s = "  Hello, World!  "
print(s.strip())                    # remove surrounding spaces
print(s.lower(), s.upper())
print("hello world".title())
print("hello world".capitalize())
print(s.replace("World", "Python"))
print("a,b,c".split(","))
print("-".join(["2026", "11", "02"]))
print("banana".count("a"))
print("banana".find("n"))            # index or -1
print("banana".index("n"))           # index or ValueError
print("python".startswith("py"), "python".endswith("on"))

# ---------- Checking content ----------
print("\n--- checks ---")
print("abc123".isalnum())
print("abc".isalpha())
print("123".isdigit())
print("   ".isspace())
print("Hello".islower(), "hello".islower())

# ---------- Formatting ----------
print("\n--- formatting ---")
name, score = "Asha", 91.456
print(f"{name} scored {score:.2f}")
print(f"{name:>10}|")               # right align
print(f"{name:<10}|")               # left align
print(f"{name:^10}|")               # center
print(f"{1000000:,}")               # thousands separator
print(f"{0.256:.1%}")               # percent

# ---------- Escape characters and raw strings ----------
print("\n--- escapes ---")
print("Line1\nLine2")
print("Tab\tseparated")
print("She said \"hi\"")
print(r"C:\new\folder")             # raw string ignores escapes

# ---------- Multiline strings ----------
poem = """Roses are red,
Violets are blue."""
print(poem)

# ---------- Iterating and comparing ----------
for ch in "abc":
    print(ch, ord(ch))              # character -> Unicode number
print(chr(97))                      # number -> character
print("apple" < "banana")           # alphabetical comparison

# ---------- Classic programs ----------
print("\n--- programs ---")


def is_palindrome(word):
    cleaned = "".join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))


def count_vowels(word):
    return sum(1 for c in word.lower() if c in "aeiou")


print(count_vowels("Programming"))

sentence = "the quick brown fox"
print(" ".join(w.capitalize() for w in sentence.split()))

freq = {}
for ch in "mississippi":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
