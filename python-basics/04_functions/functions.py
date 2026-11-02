"""Topic 4: Functions (parameters, return values, scope, lambda, recursion)."""


# ---------- Basic function ----------
def greet(name):
    """Print a greeting (docstring describes the function)."""
    print(f"Hello, {name}!")


greet("Zorshu")


# ---------- Return values ----------
def add(a, b):
    return a + b


print("add(3, 4) =", add(3, 4))


def min_max(numbers):
    return min(numbers), max(numbers)    # returns a tuple


low, high = min_max([4, 9, 1, 7])
print("min/max:", low, high)


# ---------- Default and keyword arguments ----------
def power(base, exponent=2):
    return base ** exponent


print(power(5))                 # uses default exponent
print(power(2, 10))
print(power(exponent=3, base=4))  # keyword arguments, any order


# ---------- *args and **kwargs ----------
def total(*args):
    """Accept any number of positional arguments."""
    return sum(args)


print(total(1, 2, 3, 4, 5))


def show_profile(**kwargs):
    """Accept any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_profile(name="Zorshu", course="AIML", year=1)


# ---------- Scope ----------
counter = 0


def increment():
    global counter              # modify a global variable
    counter += 1


increment()
increment()
print("counter =", counter)


def outer():
    message = "outer variable"

    def inner():
        print("inner sees:", message)   # closure

    inner()


outer()


# ---------- Lambda functions ----------
square = lambda x: x * x
print("square(6) =", square(6))

students = [("Asha", 88), ("Ravi", 92), ("Meera", 79)]
students.sort(key=lambda s: s[1], reverse=True)
print("sorted by marks:", students)

# ---------- map, filter ----------
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))


# ---------- Recursion ----------
def factorial(n):
    if n <= 1:                  # base case
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("factorial(6) =", factorial(6))
print("fibonacci(10) =", fibonacci(10))


# ---------- Type hints ----------
def area(width: float, height: float) -> float:
    return width * height


print("area =", area(3.5, 2))


# ---------- Decorator (preview) ----------
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@shout
def hello():
    return "hello world"


print(hello())
