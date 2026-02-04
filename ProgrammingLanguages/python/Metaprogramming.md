# Metaprogramming
Metaprogramming in Python allows you to write code that can manipulate code itself, creating new code, modifying existing code, or analyzing code structures. 

## Prerequisites for learning decorators
Before we learn about decorators, we need to understand a few important concepts related to Python functions. Also, remember that everything in Python is an object, even functions are objects.

### Nested Function
We can include one function inside another, known as a nested function. 

```python
def make_multiplier(n):
    # This is the nested function
    def multiply(x):
        return x * n  # 'n' is remembered by the inner function 
    return multiply

# Create specific functions using nested logic
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # result: 20
print(triple(10)) # result: 30

```

In this example, the internal function remembers the state of the external function's local variables, even after the external function has finished executing. This is known as a **closure**.

- **Reasons to use nested functions**
    - **Encapsulation**: There are times when you want to prevent a function or the data it has access to from being accessed from other parts of your code, so you can encapsulate it within another function. 
    - **Closure**: The internal function remembers the state of the external function's local variables, even after the external function has finished executing.


### Pass function as argument
We can pass a function as an argument to another function in Python. 

```python
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10
```

## Decorators

Decorators are functions that modify the behavior of other functions or classes. They wrap the target function or class and provide additional functionality. Decorators use the @ symbol and can be applied to functions or classes. Example:

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Karishma"))
```

