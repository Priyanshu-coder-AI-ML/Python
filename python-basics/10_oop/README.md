# 10 - Object-Oriented Programming (OOP)

Run it: `python oop.py`

## What you learn

### Classes and objects
A **class** is a blueprint; an **object** (instance) is something built from it.

```python
class Student:
    def __init__(self, name):
        self.name = name
```
- `__init__` is the constructor and runs when an object is created
- `self` refers to the current object
- **Instance attributes** (`self.name`) belong to one object; **class attributes** are shared by all

### Four pillars
1. **Encapsulation** - bundle data with the methods that use it and protect it. A leading underscore (`_balance`) signals "internal", and `@property` gives controlled access.
2. **Inheritance** - a child class reuses a parent: `class Dog(Animal)`. Use `super()` to call the parent.
3. **Polymorphism** - the same method name behaves differently per class (method overriding).
4. **Abstraction** - hide details and define a required interface with `ABC` and `@abstractmethod`.

### Method types
| Type | Decorator | First argument | Use |
|------|-----------|----------------|-----|
| instance | none | `self` | work with one object |
| class | `@classmethod` | `cls` | alternative constructors |
| static | `@staticmethod` | none | utility tied to the class |

### Magic (dunder) methods
`__str__`, `__repr__`, `__add__`, `__eq__`, `__len__` and others let your objects work with `print`, `+`, `==`, `len()` and more.

### Dataclasses
`@dataclass` generates `__init__`, `__repr__` and `__eq__` automatically for simple data containers.

### Helpful checks
`isinstance(obj, Class)` and `issubclass(Child, Parent)`.

## Practice
1. Build a `Library` with `Book` objects and borrow/return methods.
2. Create a `Vehicle` parent with `Car` and `Bike` children.
3. Write a `Fraction` class that supports `+`.
