# asyncio
    - Asyncio is NOT multithreading or multiprocessing.
    - It runs in a single thread, single process by default.
    - But conceptually, it feels like multithreading because it can handle multiple tasks “at the same time” by switching 
    between them whenever one is waiting (like I/O).
    - And it leverages the idea behind concurrency, similar to how threads would let the CPU do other work while one thread is blocked.

| Feature                | Multithreading                    | Multiprocessing                   | Asyncio                                            |
| ---------------------- | --------------------------------- | --------------------------------- | -------------------------------------------------- |
| Threads/Processes      | Multiple threads                  | Multiple processes                | Single thread, single process                      |
| Memory                 | Shared                            | Separate                          | Shared (single thread)                             |
| Parallel CPU execution | Limited (GIL in CPython)          | True parallelism (multi-core)     | None (single thread)                               |
| I/O handling           | Good (can block while others run) | Good (can block while others run) | Excellent (cooperative multitasking, non-blocking) |
| Ideal for              | I/O-bound tasks                   | CPU-bound tasks                   | I/O-bound tasks                                    |

