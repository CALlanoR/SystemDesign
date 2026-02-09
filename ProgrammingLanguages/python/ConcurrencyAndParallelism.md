# The Fundamental Difference: Concurrency vs Parallelism
- **Concurrency** means managing multiple tasks at once, switching between them efficiently (like juggling multiple conversations).
- **Parallelism** means executing multiple tasks simultaneously on different CPU cores (like having multiple people each handling their own conversation).

## Multiprocessing 
- True Parallel Power
- Multiprocessing sidesteps the GIL by creating separate Python processes, each with its own interpreter and memory space. This enables true parallel execution on multiple CPU cores.

### Processes
A process is an independent running program.

#### Key characteristics
- Has its own memory space
- Does not share variables with other processes
- More isolated and safer
- Heavier to create and manage

Example:

```python
from multiprocessing import Process
import os

def task():
    print("Process ID:", os.getpid())

if __name__ == "__main__":
    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

- Processes do not share variables
    - It means each process has its own separate memory space.
    - A variable in one process cannot be accessed directly by another process.
    - Changing a variable in one process does not affect the same variable in another process.

- Memory isolation
    - Each process gets its own copy of all variables.
    - Think of each process as living in a separate house. The furniture (variables) in one house cannot be touched by people in another house.

Example:

```python
from multiprocessing import Process

def change_var(x):
    x += 5
    print("Inside process:", x)

if __name__ == "__main__":
    var = 10
    p = Process(target=change_var, args=(var,))
    p.start()
    p.join()

    print("In main process:", var)


### OUTPUT
Inside process: 15
In main process: 10
```

- **When to Use Processes in Python**
    - Best for CPU-bound tasks, where heavy computation is involved.
    - Heavy calculations (Mathematical)
    - Data analysis
    - Machine learning
    - Data processing
    - Image manipulation

- **Avoid for:**
    - I/O-bound tasks (overhead isn’t worth it)
    - Tasks requiring frequent inter-process communication
    - Memory-intensive operations (each process duplicates memory)

- **Multiprocessing Limitations**
    - High memory overhead: Each process duplicates the entire Python interpreter
    - Slower startup: Creating processes is expensive (milliseconds vs microseconds for threads)
    - Complex data sharing: Inter-process communication requires serialization
    - Not for I/O: Overhead makes it slower than threading or AsyncIO for I/O tasks

Another example:

```python
from multiprocessing import Pool
import time

def cpu_intensive_task(n):
    """Simulate CPU-bound work"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

def main():
    numbers = [10000000] * 8
    
    # Sequential execution
    start = time.time()
    results_seq = [cpu_intensive_task(n) for n in numbers]
    sequential_time = time.time() - start
    
    # Parallel execution
    start = time.time()
    with Pool() as pool:
        results_par = pool.map(cpu_intensive_task, numbers)
    parallel_time = time.time() - start
    
    print(f"Sequential: {sequential_time:.2f}s")
    print(f"Parallel: {parallel_time:.2f}s")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x")

main()
```


## Threading
- The Middle Ground Solution
- Threading allows multiple threads to exist within a single process, sharing the same memory space. Python’s threading is limited by the Global Interpreter Lock (GIL), which means only one thread executes Python bytecode at a time.
- Threads run concurrently but not in parallel (for CPU-bound tasks). The operating system schedules thread execution, automatically switching between them. This makes threading great for I/O-bound work where threads spend time waiting anyway.

### Threads
A thread is a smaller unit of execution inside a process.

- **Key characteristics**
    - Threads share the same memory
    - Faster to create than processes
    - Easier to share data
    - Less isolation (one thread can affect others)
    - In Python, threads run within the same Python interpreter.

```python
from threading import Thread
import os

def task():
    print("Thread running in process:", os.getpid())

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

- **When to Use Threads in Python**
    - Best for I/O-bound tasks, where the program waits a lot.
    - Network calls
    - File reading/writing
    - Web scraping
    - APIs and database calls
- **Avoid for**
    - CPU-intensive number crunching
    - Large-scale concurrent I/O (use AsyncIO instead)
    - Tasks requiring true parallel execution
- **Threading Limitations**
    - GIL restrictions: No true parallelism for CPU-bound Python code
    - Race conditions: Shared state requires careful synchronization with locks
    - Memory overhead: Each thread consumes memory (typically 1–8 MB per thread)
    - Limited scalability: Creating thousands of threads causes performance degradation

#### Lock vs RLock
- When working with threads, multiple threads often need to access the same data.
- To avoid problems like race conditions, Python gives us locks.
- The two most common ones are:
    - threading.Lock
    - threading.RLock

- **Lock**
- A Lock allows only one thread to enter a critical section at a time.
- Rules of Lock:
    - A thread can acquire it once
    - If the same thread tries to acquire it again → deadlock

```python
import threading

lock = threading.Lock()

def outer():
    lock.acquire()
    print("Outer function")
    inner()
    lock.release()

def inner():
    lock.acquire()     # DEADLOCK
    print("Inner function")
    lock.release()

t = threading.Thread(target=outer)
t.start()
t.join()
```

- What happens here?
    - outer() acquires the lock
    - inner() tries to acquire the same lock
    - The thread blocks forever
    - Even though it’s the same thread, it cannot re-acquire the lock.

- **RLock**
- RLock stands for Reentrant Lock.
- A reentrant lock allows the same thread to acquire the lock multiple times.
- Internally, RLock:
    - Remembers which thread owns the lock
    - Keeps a count of how many times it was acquired
    - The lock is released only when the count goes back to zero.

Example:
```python
import threading

lock = threading.RLock()

def outer():
    lock.acquire()
    print("Outer function")
    inner()
    lock.release()

def inner():
    lock.acquire()     # OK
    print("Inner function")
    lock.release()

t = threading.Thread(target=outer)
t.start()
t.join()

'''Execution flow:
outer() acquires lock (count = 1)
inner() acquires lock (count = 2)
inner() releases lock (count = 1)
outer() releases lock (count = 0)
'''
```
- Using RLock with with (best practice)

```python
lock = threading.RLock()

def outer():
    with lock:
        inner()

def inner():
    with lock:
        print("Safe re-entry")
```


- This is:
    - Cleaner
    - Safer
    - Automatically releases the lock

- **When do you actually need RLock**
Use RLock when:
- A function acquires a lock
- That function calls another function
- The inner function also needs the same lock

- **Common cases**
    - Recursive functions
    - Class methods calling other methods

## AsyncIO
- The Speed Demon for I/O-Bound Tasks
- AsyncIO is Python’s modern approach to asynchronous programming. It allows you to write concurrent code using the async/await syntax, perfect for handling thousands of I/O operations without creating thousands of threads.
- AsyncIO uses a single-threaded event loop that switches between tasks whenever they’re waiting for I/O operations (network requests, file operations, database queries). While one task waits, another runs — no context switching overhead, no thread management headaches.

Example:

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [f'https://api.example.com/data/{i}' for i in range(100)]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    return results

# Run the async code
start = time.time()
asyncio.run(main())
print(f"AsyncIO: {time.time() - start:.2f} seconds")
```

- **When to Use AsyncIO**
   - Web scraping and API calls
   - Database queries with async drivers
   - WebSocket connections
   - File I/O operations
   - Microservices with thousands of concurrent connections
   - Real-time data streaming
- **Avoid for**
   - CPU-intensive calculations
   - Image/video processing
   - Data science computations
   - Any task that requires significant CPU time
- **AsyncIO Advantages**
    - Minimal memory footprint: One thread handles thousands of tasks
    - Excellent scalability: Handle 10,000+ concurrent connections easily
    - No race conditions: Single-threaded nature eliminates common concurrency bugs
    - Modern Python syntax: Clean, readable code with async/await
- **AsyncIO Limitations**
    - Requires async-compatible libraries (can’t use standard requests, need aiohttp)
    - Steeper learning curve for beginners
    - Doesn’t provide true parallelism for CPU-bound work
    - One blocking operation can freeze the entire event loop


## The Decision Matrix: Quick Reference Guide
Decision tree:
- **Your task is I/O-bound (network, disk, database):**
    - Need to handle 1000+ concurrent operations? → AsyncIO
    - Using libraries without async support? → Threading
    - Simple script with < 50 concurrent operations? → Threading
- **Your task is CPU-bound (computation, processing):**
    - Pure Python calculations? → Multiprocessing
    - Using NumPy/scientific libraries that release GIL? → Threading might work
    - Need maximum performance? → Multiprocessing
- **Your task is mixed (I/O + CPU):**
    - Mostly I/O with some CPU work? → AsyncIO or Threading
    - Significant CPU work? → Multiprocessing with async/thread workers

## Combining Approaches: The Hybrid Strategy
Example: 

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_intensive_work(data):
    # Heavy computation
    return sum(i**2 for i in range(data))

async def fetch_and_process():
    # AsyncIO for I/O
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com/data') as response:
            data = await response.json()
    
    # Multiprocessing for CPU work
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        results = await loop.run_in_executor(
            executor, 
            cpu_intensive_work, 
            data['value']
        )
    
    return results
```

## Best Practices for Each Approach
- **AsyncIO Best Practices**
    - Use connection pooling for database and HTTP clients
    - Set timeouts for all async operations
    - Use asyncio.gather() for concurrent task execution
    - Implement proper error handling with try/except in async functions
    - Use asyncio.create_task() for fire-and-forget operations
- **Threading Best Practices**
    - Use thread pools (ThreadPoolExecutor) instead of manual thread management
    - Always join threads to ensure completion
    - Use threading locks to protect shared state
    - Keep thread count reasonable (10–50 for most applications)
    - Use thread-safe data structures like queue.Queue
- **Multiprocessing Best Practices**
    - Use process pools to avoid repeated process creation overhead
    - Minimize data transfer between processes
    - Use shared memory for large datasets
    - Handle process cleanup with context managers
    - Consider using multiprocessing.Queue for inter-process communication