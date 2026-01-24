# Reliability
- Reliability refers to the ability of a system to continue operating correctly and effectively in the presence of faults, errors, or failures. In simple terms, a distributed system is considered reliable if it keeps delivering its services even when one or several of its software or hardware components fail. Reliability represents one of the main characteristics of any distributed system, since in such systems any failing machine can always be replaced by another healthy one, ensuring the completion of the requested task.
- A related concept is Fault Tolerance, which is the system’s ability to continue operating (possibly at a reduced level) even when one or more of its components fail. In other words, it is the property that allows a system to absorb or recover from faults without total breakdown.

## The Difference Between Reliability and Fault Tolerance
Although these terms often overlap, the main differences can be summarized as follows:

    Scope:
        Reliability focuses on the end-to-end correctness and consistency of the entire system’s operation over time.
        Fault tolerance focuses on the system’s ability to continue operating when individual components fail.

    Perspective:
        Reliability is primarily a user-centric concept: Can the system consistently meet the user’s expectations over time?
        Fault tolerance is more of a system-centric concept: How does the system handle internal failures or component breakdowns?

    Measurement:
        Reliability is often measured in terms of uptime, error rates, or mean time between failures (MTBF).
        Fault tolerance is often measured by how quickly and effectively the system detects, isolates, and recovers from failures (e.g., failover times).
