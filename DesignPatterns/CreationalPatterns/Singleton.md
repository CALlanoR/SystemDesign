# Singleton
- Have one single instance of a class.
- Example:
    - Graphics device manager
    - Pool manager
    - Logger
    - Event Manager
- Not all languages support to create a singleton pattern, some languages need more complicated setup to make it work.
- C++ have multiple constructors incluiding a copy constructor and operator overloading may also create new instances (you need to block all those things)
- Python doesn't have access modifiers, so you can't make the initializer private

## Dark Side of Singleton Pattern (Antipattern)
- SOLID principles ensures that software systems remain robust, scalable, and adaptable to evolving requirements.
    - Violates Single Responsibility Principle
        - A Singleton is responsible for both managing its instance lifecycle and business logic, leading to a violation of SRP.
    - Violates Open/Closed Principle
        - Singletons are often implemented with private constructors, making them not possible to extend or difficult to modify without altering the existing class.
    - Violates Dependency Inversion Principle
        - High-level modules should depend on abstractions rather than concrete implementations. However, a Singleton forces dependencies on a concrete class, making it harder to replace or substitute.
- Concurrency Issues: In multi-threaded environments, access to the single instance must be carefully managed to avoid race condition

- Example with python using metaclasses:
```
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating Logger")
    
    def log(self, msg):
        print(msg)

class CustomLogger(Logger):
    def __init__(self):
        print("Creating Custom logger")
        super().__init__()

logger = CustomLogger()
logger2 = CustomLogger()
print(logger)
print(logger2)
logger.log("Hello")
logger2.log("Helloooo")
```