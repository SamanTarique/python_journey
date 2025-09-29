##### Thread's methods
    - start() - Starts the thread’s activity. Must be called exactly once.
    - run()
    - join() - Waits for the thread to finish.
    - is_alive() - Returns True if the thread is still running.
    - getName() - Get/set the thread’s name. Helpful for logging debugging.
    - setName() - Get/set the thread’s name. Helpful for logging/debugging.

##### synchronization primitives / Safe communication techniques

    - Lock() - a Lock is a synchronization primitive used to control access to shared resources in multithreaded programs. 
    It ensures that only one thread at a time can access a particular block of code or resource, preventing race 
    conditions.

    - RLock() - An RLock (Reentrant Lock) in Python is a special kind of lock that allows the same thread to acquire it 
    multiple times without causing a deadlock. Regular Lock cannot be acquired recursively by the same thread—if a thread 
    tries, it will block itself and deadlock.

    - Semaphore(<int>) - A Semaphore in Python is another synchronization primitive like a Lock, but it’s a counter-based 
    lock. Instead of only allowing one thread at a time, it allows up to a fixed number of threads to access a shared 
    resource simultaneously.

    * Think of it like a parking lot with limited spaces:

        - If the lot has 3 spots, up to 3 cars (threads) can enter at the same time.

        - If all spots are full, new cars must wait until a spot is free.
    
    - Queue - a Queue is a thread-safe data structure used to safely exchange data between threads (or even processes). It
     handles the synchronization for you, so you don’t have to manually use locks when multiple threads are producing or 
     consuming items.

