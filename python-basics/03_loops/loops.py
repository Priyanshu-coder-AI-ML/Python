"""Topic 3: Loops (for, while, break, continue, nested loops)."""

# ---------- for loop with range ----------
print("--- range ---")
for i in range(5):               # 0..4
    print(i, end=" ")
print()

for i in range(1, 11, 2):        # start, stop, step
    print(i, end=" ")
print()

for i in range(5, 0, -1):        # counting down
    print(i, end=" ")
print()

# ---------- Looping over a sequence ----------
print("\n--- sequences ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

for ch in "Python":
    print(ch, end=" ")
print()

names = ["Asha", "Ravi", "Meera"]
scores = [88, 92, 79]
for n, s in zip(names, scores):
    print(f"{n}: {s}")

# ---------- while loop ----------
print("\n--- while ---")
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Liftoff!")

# ---------- break and continue ----------
print("\n--- break / continue ---")
for i in range(1, 11):
    if i == 4:
        continue                 # skip 4
    if i == 8:
        break                    # stop at 8
    print(i, end=" ")
print()

# ---------- for / else ----------
print("\n--- for-else ---")
for n in range(2, 10):
    if n == 7:
        print("Found 7")
        break
else:
    print("7 not found")         # runs only if loop was not broken

# ---------- Nested loops ----------
print("\n--- multiplication table ---")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")
    print()

print("\n--- star pattern ---")
for i in range(1, 6):
    print("*" * i)

# ---------- Classic examples ----------
total = 0
for n in range(1, 101):
    total += n
print("\nSum 1..100 =", total)

n = 5
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Fibonacci
a, b = 0, 1
fib = []
while len(fib) < 10:
    fib.append(a)
    a, b = b, a + b
print("Fibonacci:", fib)

# Prime check
num = 29
is_prime = num > 1
for d in range(2, int(num ** 0.5) + 1):
    if num % d == 0:
        is_prime = False
        break
print(f"{num} is prime:", is_prime)
