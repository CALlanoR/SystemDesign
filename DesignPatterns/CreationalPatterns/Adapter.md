# Adapter
- The Adapter pattern is a structural design pattern that facilitates the interaction between two interfaces that are incompatible or cannot work together directly. It acts as a bridge, allowing objects with different interfaces to collaborate.

- Components:
    - **Client Interface:** An interface that specifies the functions that the client should implement.
    - **Client:** A class that implements the client interface.
    - **Adaptee/Service:** The incompatible class that needs to collaborate with the client interface.
    - **Adapter:** The class that makes the collaboration between the service and the client possible.

## Example

```sh
class OldSystem:
    def legacy_operation(self):
        return "Legacy operation"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self):
        return f"Adapter: {self.old_system.legacy_operation()}"

# Client code
def client_code(adapter):
    result = adapter.new_operation()
    print(result)

if __name__ == "__main__":
    old_system = OldSystem()
    adapter = Adapter(old_system)
    client_code(adapter)
```

[View more examples (from https://github.com/ArjanCodes)](https://github.com/CALlanoR/SystemDesign/blob/main/DesignPatterns/CreationalPatterns/Examples/Adapter)

## Pros and Cons of Adapter Design Pattern

The advantages of Adapter Patterns are:

- We can achieve low coupling between the adapter class and the client class.
- We can reuse the adapter class to incorporate numerous service classes in the application.
- We can increase the flexibility of the program by introducing multiple adapters without interfering with the client code

The disadvantages of Adapter Pattern are:

- The program's complexity increases with the addition of adapter class and service class.
- There is an increase of overhead in the program as the requests are forwarded from one class to another.
- Adapter Pattern(class adapter) uses multiple inheritance, which all the programming languages may not support.
