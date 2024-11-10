# Control Resource Demand
One way to increase performance is to carefully manage the demand for resources. This can be done by reducing the number of events processed or by limiting the rate at which the system responds to events.

## Limit event response
When discrete events arrive at the system (or component) too rapidly to be processed, then the events must be queued until they can be processed, or they are simply discarded. You may choose to process events only up to a set maximum rate, thereby ensuring predictable processing for the events that are actually processed.

This tactic could be triggered by a queue size or processor utilization exceeding some warning level.

- Queues
    - Queues are a fundamental building block in messaging systems designed for one-to-one communication. In a queue-based architecture, messages are sent to a specific queue and processed by a single receiver. The sender and receiver operate independently, allowing for asynchronous and decoupled communication.
    - Key characteristics of queues include:
        - **Message persistence:** Queues typically store messages until they are consumed by a receiver. This ensures reliable message delivery even if the receiver is temporarily unavailable.
        - **Point-to-point communication:** Each message in a queue is consumed by a single receiver. Once a receiver consumes a message, it is removed from the queue, preventing other consumers from processing it.
        - **Ordering guarantee:** Queues preserve the order of messages, ensuring that they are processed in the order they were added to the queue. This is particularly important in scenarios where message order is critical.
    - Use cases for queues:
        - **Task distribution:** Queues are commonly used for distributing tasks among multiple workers in a load-balanced manner. Each worker consumes a task from the queue, processes it, and removes it from the queue.
        - **Event-driven architectures:** Queues facilitate event-driven communication between microservices, where events are published to a queue and consumed by interested subscribers.
- Topics
    - Topics, on the other hand, are designed for one-to-many communication scenarios. In a topic-based architecture, messages are published to a topic and can be consumed by multiple subscribers who have an interest in receiving those messages. Topics allow for broadcast-style communication, where messages are delivered to all interested parties.
    - Key characteristics of topics include:
        - **Publish/subscribe model:** Messages published to a topic are broadcasted to all subscribers interested in receiving them. Subscribers operate independently and consume messages at their own pace.
        - **Message filtering:** Topics often provide the ability to filter messages based on content, allowing subscribers to receive only the messages that match specific criteria. This enables efficient and selective message consumption.
        - **Message durability:** Topics typically retain messages for a certain period or until they are explicitly acknowledged by subscribers. This ensures that even if a subscriber is temporarily offline, it can still receive messages published during its absence.
    - Use cases for topics:
        - **Event-driven architectures:** Topics are widely used in event-driven architectures, where events are published to a topic, and multiple subscribers consume the events based on their interests. This enables loose coupling and scalability in distributed systems.
        - **Real-time data streaming:** Topics are suitable for scenarios where real-time data needs to be streamed to multiple consumers, such as real-time analytics or IoT applications.


Sources: 
- https://medium.com/version-1/queues-vs-topics-understanding-the-differences-in-messaging-frameworks-88861e2effa8

