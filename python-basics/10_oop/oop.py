"""Topic 10: Object-oriented programming."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ---------- Class, object, constructor ----------
class Student:
    school = "Parul University"              # class attribute (shared)

    def __init__(self, name, marks):
        self.name = name                     # instance attributes
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):                       # readable text for print()
        return f"Student({self.name}, avg={self.average():.1f})"

    def __repr__(self):                      # developer-friendly text
        return f"Student(name={self.name!r}, marks={self.marks!r})"


s1 = Student("Asha", [80, 90, 85])
print(s1)
print(s1.average())
print(Student.school)

# ---------- Encapsulation ----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance              # _ = "internal use" convention

    @property
    def balance(self):                       # read-only access
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


acct = BankAccount("Ravi", 1000)
acct.deposit(500)
acct.withdraw(200)
print("\nBalance:", acct.balance)


# ---------- Inheritance and polymorphism ----------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    def speak(self):                         # method overriding
        return "Woof"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)               # call parent constructor
        self.indoor = indoor

    def speak(self):
        return "Meow"


print()
for pet in (Dog("Bruno"), Cat("Kitty"), Animal("Thing")):
    print(pet.intro())                       # same call, different behavior

print(isinstance(Dog("x"), Animal), issubclass(Cat, Animal))


# ---------- Abstract classes ----------
class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


print()
for shape in (Rectangle(3, 4), Circle(2)):
    print(type(shape).__name__, round(shape.area(), 2))


# ---------- Class and static methods ----------
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):             # alternative constructor
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_freezing(c):                      # no access to self or cls
        return c <= 0


print("\n", Temperature.from_fahrenheit(212).celsius)
print(Temperature.is_freezing(-4))


# ---------- Magic (dunder) methods ----------
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __len__(self):
        return 2

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


print(Vector(1, 2) + Vector(3, 4), Vector(1, 1) == Vector(1, 1))


# ---------- Dataclass ----------
@dataclass
class Point:
    x: float
    y: float = 0.0


print(Point(3), Point(1, 2) == Point(1, 2))
