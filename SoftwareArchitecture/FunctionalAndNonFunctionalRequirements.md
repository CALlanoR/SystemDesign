# Functional vs. Non-functional Requirements
## Functional Requirements
- Definition: These are the requirements that define what a system is supposed to do. They describe the various functions that the system must perform.
- Examples:
    - A user authentication system must validate user credentials and provide access levels.
    - An e-commerce website should allow users to browse products, add them to a cart, and complete purchases.
    - A report generation system must collect data, process it, and generate timely reports.

## Non-Functional Requirements
- Definition: These requirements describe how the system performs a task, rather than what tasks it performs. They are related to the quality attributes of the system.
- Examples:
    - Scalability: The system should handle growth in users or data.
    - Performance: The system should process transactions within a specified time.
    - Availability: The system should be up and running a defined percentage of time.
    - Security: The system must protect sensitive data and resist unauthorized access.
- When you are analyzing projects, here's how you can handle these requirements:
    1. Clarify Requirements: Start by asking questions to understand both functional and non-functional requirements. Interviewers often leave these vague to see if you'll probe for more details.
    2. Prioritize: Not all requirements are equally important. Identify which ones are critical for the system’s success.
    3. Trade-offs: Discuss trade-offs related to different architectural decisions, especially concerning non-functional requirements. For example, a system highly optimized for read operations might have slower write operations.
    4. Use Real-World Examples: If you can, relate your points to real-world systems or your past experiences. This shows practical understanding.
    5. Balance: Ensure you're not focusing too much on one type of requirement over the other. A well-rounded approach is often necessary.

# What are Back-of-the-Envelope Estimations?
During a system design interview, your ability to make quick estimations is essential for several reasons:
- Indicates System Scalability: Highlights your understanding of how the system can grow or adapt.
- Validate proposed solutions: Estimation helps you ensure that your proposed architecture meets the requirements and can handle the expected load.
- Identify bottlenecks: Quick calculations help you identify potential performance bottlenecks and make necessary adjustments to your design.
- Demonstrate your thought process: Estimation showcases your ability to make informed decisions and trade-offs based on a set of assumptions and constraints.
- Communicate effectively: Providing estimates helps you effectively communicate your design choices and their implications to the interviewer.
- Quick Decision Making: Reflects your ability to make swift estimations to guide your design decisions.


## Estimation Techniques
1. Rule of thumb
    - Rules of thumb are general guidelines or principles that can be applied to make quick and reasonably accurate estimations. They are based on experience and observation, and while not always precise, they can provide valuable insights in the absence of detailed information. For example, estimating that a user will generate 1 MB of data per day on a social media platform can serve as a starting point for capacity planning.
2. Approximation
    - Approximation involves simplifying complex calculations by rounding numbers or using easier-to-compute values. This technique can help derive rough estimates quickly and with minimal effort. For instance, assuming 1,000 users instead of 1,024 when estimating storage requirements can simplify calculations and still provide a reasonable approximation.
3. Breakdown and aggregation
    - Breaking down a problem into smaller components and estimating each separately can make it easier to derive an overall estimate. This technique involves identifying the key components of a system, estimating their individual requirements, and then aggregating these estimates to determine the total system requirements. For example, estimating the storage needs for user data, multimedia content, and metadata separately can help in determining the overall storage requirements of a social media platform.
4. Sanity check
    - A sanity check is a quick evaluation of an estimate to ensure its plausibility and reasonableness. This step helps identify potential errors or oversights in the estimation process and can lead to more accurate and reliable results. For example, comparing the estimated storage requirements for a messaging service with the actual storage used by a similar existing service can help validate the estimate.

### Process
- Understand the Scope: Clarify the scale of the problem - how many users, how much data, etc.
- Use Simple Math: Utilize basic arithmetic to estimate the scale of data and resources.
- Round Numbers for Simplicity: Use round numbers to make calculations easier and faster.
- Be Logical and Reasonable: Ensure your estimations make sense given the context of the problem.


### Practical Examples
1. Load Estimation

    Suppose you’re asked to design a social media platform with 100 million daily active users (DAU) and an average of 10 posts per user per day. To estimate the load, you’d calculate the total number of posts generated daily:

        100 million DAU * 10 posts/user = 1 billion posts/day

    Then, you can estimate the request rate per second:

        1 billion posts/day / 86,400 seconds/day ≈ 11,574 requests/second


2. Storage Estimation

    Consider a photo-sharing app with 500 million users and an average of 2 photos uploaded per user per day. Each photo has an average size of 2 MB. To estimate the storage required for one day’s worth of photos, you’d calculate:

        500 million users * 2 photos/user * 2 MB/photo = 2,000,000,000 MB/day


3. Bandwidth Estimation

    For a video streaming service with 10 million users streaming 1080p videos at 4 Mbps, you can estimate the required bandwidth:

        10 million users * 4 Mbps = 40,000,000 Mbps


4. Latency Estimation

    Suppose you’re designing an API that fetches data from multiple sources, and you know that the average latency for each source is 50 ms, 100 ms, and 200 ms, respectively. If the data fetching process is sequential, you can estimate the total latency as follows:

        50 ms + 100 ms + 200 ms = 350 ms

    If the data fetching process is parallel, the total latency would be the maximum latency among the sources:

        max(50 ms, 100 ms, 200 ms) = 200 ms


5. Resource Estimation

    Imagine you’re designing a web application that receives 10,000 requests per second, with each request requiring 10 ms of CPU time. To estimate the number of CPU cores needed, you can calculate the total CPU time per second:

        10,000 requests/second * 10 ms/request = 100,000 ms/second

    Assuming each CPU core can handle 1,000 ms of processing per second, the number of cores required would be:

        100,000 ms/second / 1,000 ms/core = 100 cores
