"""Topic 1: Variables, data types, input/output and operators."""

# ---------- Variables ----------
name = "Zorshu"          # str
age = 18                 # int
height = 1.75            # float
is_student = True        # bool
nothing = None           # NoneType

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
print("Nothing:", nothing)

# ---------- Checking types ----------
print("\n--- Types ---")
for value in (name, age, height, is_student, nothing, 3 + 4j):
    print(f"{value!r:>10} -> {type(value).__name__}")

# ---------- Type conversion (casting) ----------
print("\n--- Type conversion ---")
print(int("42") + 8)         # str -> int
print(float("3.14") * 2)     # str -> float
print(str(100) + " rupees")  # int -> str
print(bool(0), bool(""), bool("hi"), bool([]))  # truthy / falsy
print(int(7.9))              # float -> int (truncates, does not round)

# ---------- Multiple assignment ----------
a, b, c = 1, 2, 3
x = y = z = 0
a, b = b, a                  # swap without a temp variable
print("\na, b =", a, b)

# ---------- Arithmetic operators ----------
print("\n--- Arithmetic ---")
p, q = 17, 5
print("p + q  =", p + q)
print("p - q  =", p - q)
print("p * q  =", p * q)
print("p / q  =", p / q)     # true division -> float
print("p // q =", p // q)    # floor division
print("p % q  =", p % q)     # remainder
print("p ** q =", p ** q)    # power

# ---------- Comparison and logical operators ----------
print("\n--- Comparison & logic ---")
print(p > q, p == q, p != q)
print(p > 10 and q < 10)
print(p > 20 or q < 10)
print(not (p > q))

# ---------- Assignment operators ----------
n = 10
n += 5
n *= 2
n -= 3
print("\nn =", n)

# ---------- Output formatting ----------
print("\n--- Output formatting ---")
print(f"{name} is {age} years old and {height:.1f} m tall")
print("{} is {} years old".format(name, age))
print("%s is %d years old" % (name, age))
print("a", "b", "c", sep="-", end="!\n")

# ---------- Input (uncomment to try) ----------
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello {user_name}, next year you will be {user_age + 1}")
