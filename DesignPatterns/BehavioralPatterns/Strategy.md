# Strategy Pattern
- The Strategy Pattern is all about choosing how to do something without changing the rest of the system.
- Example in python:
```python
from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(NotificationStrategy):
    def send(self, message: str):
        print(f"Sending EMAIL: {message}")

class SlackNotification(NotificationStrategy):
    def send(self, message: str):
        print(f"Sending SLACK: {message}")

class SMSNotification(NotificationStrategy):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class Notifier:
    def __init__(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def notify(self, message: str):
        self._strategy.send(message)

notifier = Notifier(EmailNotification())
notifier.notify("System online")
```