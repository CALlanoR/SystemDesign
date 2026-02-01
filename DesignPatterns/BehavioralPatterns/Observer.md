# Observer
- Defines a dependency between objects, ensuring that when one object changes state, all its dependents are notified and updated automatically.
- Example in python:
```python
from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, data: str):
        pass

class LoggerSubscriber(Subscriber):
    def update(self, data: str):
        print(f"[Logger] Event received: {data}")

class AlertSubscriber(Subscriber):
    def update(self, data: str):
        print(f"[Alert] Triggering alarm for: {data}")

class Event:
    def __init__(self):
        self._subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, data: str):
        for subscriber in self._subscribers:
            subscriber.update(data)

event = Event()

log_service = LoggerSubscriber()
alert_service = AlertSubscriber()

event.subscribe(log_service)
event.subscribe(alert_service)

event.notify("Temperature exceeded threshold!")
```
