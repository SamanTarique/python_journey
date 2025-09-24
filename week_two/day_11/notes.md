##### decorator
- In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code. 

- A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality. 

- Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

- use case:
    - Logging: Track function calls (e.g., @logger).
    - Authentication: Restrict access in web apps (e.g., Flask/Django).
    - Rate Limiting: Control API usage per user.
    - Caching: Store results using functools.lru_cache.
    - Retry Logic: Automatically retry failed network calls.

- There are 3 types of decorator
    - Function decorator (for logging , auth , cachiing)
    - Method Decorator (purpose is same as Function decorator just handle the self parameter for instance methods)
    - Class Decorator (use for class level changes like adding or updating attribute values , it takes class as in parameter)

##### generator
- generator is a special type of function which returns an iterator, allowing you to iterate over it for values but lazily. lazily means once at a time. generator function uses yield keyword to return the value and pause the execution untill next call
- use case:
    - accesing data from a large dataset and also doing some operation on data, without generator, might occupy huge memory as well as take so much time.

##### iterator
- iter(iterator) is an object that return an iterator with __iter__ and __next__ , which used for getting next iterator value on demand.
- use case:
    - acces on demand data

##### In short:
    * Use list when you need random access or reuse.
    * Use generator when data is huge, infinite, or you only need it once.
