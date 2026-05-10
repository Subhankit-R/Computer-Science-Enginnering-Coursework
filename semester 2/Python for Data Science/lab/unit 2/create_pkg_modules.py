import os

# Create the mypackage directory
os.makedirs('mypackage', exist_ok=True)

# Create __init__.py
with open('mypackage/__init__.py', 'w') as f:
    f.write('''from .arithmetic import add, subtract
from .greetings import say_hello
''')

# Create arithmetic.py
with open('mypackage/arithmetic.py', 'w') as f:
    f.write('''def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
''')

# Create greetings.py
with open('mypackage/greetings.py', 'w') as f:
    f.write('''def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"
''')

# Create main.py
with open('main.py', 'w') as f:
    f.write('''from mypackage import add, say_hello
from mypackage.arithmetic import multiply, divide
from mypackage import greetings

print(add(10, 5))
print(multiply(4, 3))
print(divide(10, 2))
print(say_hello("Alice"))
print(greetings.say_goodbye("Bob"))
''')

print("Package created successfully!")