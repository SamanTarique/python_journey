##### Multithreading
    Q. What is Thread ?
    A. Thread is the smallest unit of execution that an operating system can schedule and run.
       * A process is a program in execution (it has its own memory space, resources, etc.).

       * A thread is a lightweight unit of that process — multiple threads can run inside a single process, sharing its memory
        and resources.

    * Concurrency
        - Concurrency is about dealing with multiple tasks at once, not necessarily running them at the same instant.
        - On a single-core CPU, concurrency is achieved by context switching: the CPU switches between tasks so fast it feels 
          like they’re happening together.
        - On a multi-core CPU, concurrency can turn into parallelism, where tasks truly run at the same time.
    
    * Benefits of Multithreading
        - Lightweight → Threads share the same memory space of their parent process (unlike processes, which have isolated memory).
        
        - Concurrency → Multiple threads allow tasks to run seemingly at the same time (e.g., handling user input while also performing background calculations).
        
        - Parallelism → On multi-core CPUs, different threads can literally run in parallel.

        - Independent execution → Each thread has its own execution stack, program counter, and registers, but shares code, data, and open files with other threads of the same process.

        - Faster I/O Operations: Time-consuming tasks like file reading/writing or network operations can be delegated to other threads to avoid blocking the main program flow.
    
    * Challenges of Multithreading
        - Race Conditions: When two threads try to access and modify the same data simultaneously, unexpected results may occur.
        
        - Deadlocks: Threads waiting on each other can cause the program to freeze.
    
        - Increased Code Complexity: Multithreaded code is harder to write, debug, and maintain.
    
        - Synchronization is Required: Tools like locks, mutexes, and semaphores are needed to control concurrent access to 
          shared resources.
    * GIL (Global Interpreter Lock)
        - It’s a mutex (a lock) that prevents multiple native threads from executing Python bytecode at the same time in CPython 
          (the standard Python implementation).

        - Even if your CPU has 4 cores, only one thread runs Python code at a time.

    * Why, Python’s memory management isn’t thread-safe by default.

        - The GIL makes things simpler and avoids memory corruption, but it limits parallel execution of Python code.

##### Multiprocessing
    - Python's multiprocessing module enables the execution of multiple processes in parallel, which can significantly improve
     performance for CPU-bound tasks by leveraging multiple CPU cores. Unlike multithreading, multiprocessing bypasses the 
     Global Interpreter Lock (GIL) by using separate processes, each with its own Python interpreter and memory space.

##### threads vs process
    - a process is a separate, independent instance of a running program with its own memory space, while a thread is a smaller unit of execution within a single process that shares the process's memory and resources

##### Race condition
    - Race condition occurs when multiple threads or processes read and write the same variable i.e. they have access to some shared data and they try to change it at the same time. In such a scenario threads are “racing” each other to access/change the data.

    * A race condition is a situation that may occur inside a critical section if the critical section is not properly protected.
    
    * This happens when the result of multiple thread execution in a critical section differs according to the order in which 
        the threads execute.
    
    * Race conditions in critical sections can be avoided if the critical section is treated as an atomic instruction. Also, 
        proper thread synchronization using locks or atomic variables can prevent race conditions.

    # Prevent Race condition
        # Locks
            - Locks are the most common way to prevent race conditions. A lock ensures that only one thread can access a 
            "critical section" of code (where shared resources are modified) at a time.
        
        # Queue
            - Python's queue module provides thread-safe queue implementations, which inherently help prevent race conditions 
            when multiple threads access shared data through the queue. This is because the Queue class uses internal locks to 
            manage access to its data, ensuring that operations like put() and get() are atomic.
            
            * Producer-Consumer pattern: This is a common and effective way to use queues to prevent race conditions. Producer 
            threads add items to the queue, and consumer threads retrieve and process items from the queue. The queue handles 
            the synchronization, ensuring data integrity.
            
