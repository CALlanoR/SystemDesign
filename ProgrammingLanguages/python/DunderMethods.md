# Dunder or magic methods in Python (underscore methods)
- Python magic (dunder) methods are special methods with double underscores __ that enable operator overloading and custom object behavior.
- The below code displays the magic methods inherited by int class.
    - print(dir(int))
    - dir(int) lists all attributes and methods of the int class, including magic (dunder) methods like __add__, __str__, etc.
- Python provides over 100 dunder methods, each designed to control different aspects of object behavior. While we’ve explored key categories in this article, here’s a high-level summary to serve as a quick reference:
    - **Arithmetic methods:** Methods like __add__, __sub__, __mul__, and __truediv__ allow your objects to support operators (+, -, *, /).
    - **Comparison methods:** Methods such as __eq__, __lt__, and __gt__ define how objects are compared for equality or order.
    - **Attribute management:** With methods like __getattr__, __setattr__, and __delattr__, you can control attribute access and implement dynamic behaviors.
    - **Initialization and construction:** __new__, __init__, and __del__ manage object creation, initialization, and cleanup, respectively.
    - **String representation:** Methods such as __str__ and __repr__ determine how objects are represented as strings, aiding user-friendly output.
    - **Iteration and container behavior:** Implement __iter__ and __next__ to make your objects iterable and other methods to support indexing and length retrieval.
    - **Callability:** __call__ lets an instance be called like a function, enabling a functional programming style with stateful behavior.
    - Context management: With __enter__ and __exit__, objects can be used with statements to manage resources properly.
    - **Metaprogramming hooks:** Methods like __init_subclass__ provide ways to customize class creation and behavior dynamically.
- Examples:
    - Allow your objects to work naturally with arithmetic operators.
      ```python
        class Vector:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)
        def __str__(self):
                return f"Vector({self.x}, {self.y})"

        # Usage
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)

        result = v1 + v2
        print(result)  # Output: Vector(4, 6)
        ```
    - Caching
    ```python
        class CachedComputation:
        def __init__(self):
                self.cache = {}
        def __call__(self, x):
                if x not in self.cache:
                    self.cache[x] = self._expensive_computation(x)
                return self.cache[x]
        def _expensive_computation(self, x):
                # Imagine a complex calculation here
                return x ** 2

        # Usage
        compute = CachedComputation()

        print(compute(5))  # Computes and caches: Output: 25
        print(compute(5))  # Retrieves from cache: Output: 25
    ```
    - Custom context managers
        - Building a context manager using __enter__ and __exit__ methods lets you automate resource management. For example, you can design a custom context manager to handle file operations—opening a file when you enter a block and ensuring it closes when you exit. 
    ```python
        class FileHandler:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()

        # Usage
        with FileHandler("example.txt", "r") as file:
            content = file.read()
            print(content)
    ```
    - Custom iterables and containers
        - To make your custom containers work with Python’s loops and comprehensions, implement the iteration protocol by defining methods like __iter__ and __next__. 
        ```python
        class Stack:
        def __init__(self):
            self.items = []
        def push(self, item):
            self.items.append(item)
        def pop(self):
                return self.items.pop()
        def __iter__(self):
            self.index = 0
            return self
        def __next__(self):
            if self.index >= len(self.items):
                raise StopIteration
            item = self.items[self.index]
            self.index += 1
            return item

        # Usage
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        for item in stack:
            print(item)  # Output: 1, 2, 3
    ```
        - Explanation:
            - Iteration Support:
                - **__iter__(self):** makes the Stack class iterable. It initializes an index for iteration and returns the iterator object itself (the stack instance).
                - **__next__(self):** defines how to iterate over the stack. It raises StopIteration when all items have been iterated. Otherwise, it returns the current item and increments the index.



