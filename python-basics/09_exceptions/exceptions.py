"""Topic 9: Exception handling."""

# ---------- Basic try / except ----------
print("--- basic ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# ---------- Multiple except blocks ----------
print("\n--- multiple ---")


def parse_and_divide(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print("Please give valid numbers")
    except ZeroDivisionError:
        print("Divisor cannot be zero")
    except (TypeError, KeyError) as e:      # several types at once
        print("Type problem:", e)


parse_and_divide("10", "2")
parse_and_divide("ten", "2")
parse_and_divide("10", "0")

# ---------- else and finally ----------
print("\n--- else / finally ---")
try:
    number = int("42")
except ValueError:
    print("Not a number")
else:
    print("Parsed successfully:", number)   # runs only if no exception
finally:
    print("This always runs")               # cleanup code

# ---------- Catching the error object ----------
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print("\nError message:", e)

# ---------- Raising exceptions ----------
print("\n--- raise ---")


def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


for value in (25, -3, "x"):
    try:
        print("Age set to", set_age(value))
    except (TypeError, ValueError) as e:
        print("Rejected:", e)


# ---------- Custom exceptions ----------
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""

    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} is less than {amount}")
        self.balance = balance
        self.amount = amount


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


print("\n--- custom ---")
try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print("Failed:", e)

# ---------- Re-raising and chaining ----------
print("\n--- chaining ---")
try:
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Could not load configuration") from e
except RuntimeError as e:
    print(e, "| caused by:", repr(e.__cause__))

# ---------- Input validation loop ----------
print("\n--- validation loop (simulated input) ---")
attempts = iter(["abc", "-5", "21"])        # replace with input() in real use
while True:
    raw = next(attempts)
    try:
        age = int(raw)
        if age < 0:
            raise ValueError("negative")
        print("Accepted:", age)
        break
    except ValueError:
        print(f"'{raw}' is invalid, try again")

# ---------- assert ----------
print("\n--- assert ---")
try:
    assert 2 + 2 == 5, "Math is broken"
except AssertionError as e:
    print("Assertion failed:", e)

# ---------- Common built-in exceptions ----------
# ValueError, TypeError, KeyError, IndexError, ZeroDivisionError,
# FileNotFoundError, AttributeError, NameError, ImportError, StopIteration
