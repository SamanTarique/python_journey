# for
    - A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    - With the break statement we can stop the loop before it has looped through all the items:
    - With the continue statement we can stop the current iteration of the loop, and continue with the next:
    - To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    - range() excludes the last number , like in 0 - 6 , it will run upto 5 only.
    - The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6).
    - The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
    
    ## Else in For Loop
      -The else keyword in a for loop specifies a block of code to be executed when the loop is finished

      for x in range(6):
        print(x)
      else:
        print("Finally finished!") 
      - Note: The else block will NOT be executed if the loop is stopped by a break statement.
    
    ## Nested Loops
      - A nested loop is a loop inside a loop.The "inner loop" will be executed one time for each iteration of the "outer loop":

    ## The pass Statement
      - for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

      a = [0, 1, 2]
      for element in a:
        if not element:
          pass
        print(element)

      a = [0, 1, 2]
      for element in a:
        if not element:
          pass
        print(element)
    
    * pass just simply skips the block only , while continue goes for next iteration

# while
    - While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.
    - we cant use range function here.
    - else everything is same as for

# range()
    - The Python range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequences on a sequence of numbers using Python loops.
    
    * range (stop) takes one argument.
    * range (start, stop) takes two arguments.
    * range (start, stop, step) takes three arguments.

    - The step value must not be zero. If a step is zero, python raises a ValueError exception.
    - If a user wants to decrement, then the user needs steps to be a negative number. 
    - Python range() function doesn’t support float numbers. i.e. user cannot use floating-point or non-integer numbers in any of its arguments. Users can use only integer numbers.
    
    * Accessing range() with an Index Value
      - A sequence of numbers is returned by the range() function as its object that can be accessed by its index value. Both positive and negative indexing is supported by its object.

# Memory management in Python
    - Memory management refers to process of allocating and deallocating memory to a program while it runs. Python handles memory management automatically using mechanisms like reference counting and garbage collection, which means programmers do not have to manually manage memory.

    # Reference Count
      - Every object in Python keeps track of how many references point to it.

      - This number is called the reference count.

      - When the count drops to zero, it means nothing is using the object → Python immediately frees its memory.

      import sys

      a = [10, 20, 30]
      print(sys.getrefcount(a))  # count = 2

      b = a
      print(sys.getrefcount(a))  # count = 3 (a, b, + temp call)

      del b
      print(sys.getrefcount(a))  # count = 2 again

      del a
      # now refcount = 0 → Python frees the memory

    # Circular referencing
      - A circular reference happens when two (or more) objects reference each other, so their reference counts never reach zero naturally.

      class Node:
      def __init__(self, value):
        self.value = value
        self.next = None

      # Create two nodes
      a = Node("A")
      b = Node("B")
      # Make them reference each other
      a.ref = b
      b.ref = a

      del a
      del b

      Namespace (variables)           Objects in heap
      +---------+                     +------------------+
      |   a ----|-------------------> | Node("A")        |
      |   b ----|-------------------> | Node("B")        |
      +---------+                     +------------------+


      Namespace                        Objects in heap
      +---------+                      +------------------+
      |   a ----|------------------->  | Node("A")        |
      |   b ----|------------------->  |   ref ---------->| Node("B") |
      +---------+                      |                  |   ref ----|
                                       +------------------+           |
                                                     ^----------------+

      Namespace                        Objects in heap
      +---------+                      +------------------+
      |         |   (empty)            | Node("A")        |
      |         |                      |   ref ---------->| Node("B") |
      +---------+                      |                  |   ref ----|
                                      +------------------+           |
                                                    ^----------------+

    # Garbage Collection
      - It is a process in which Python automatically frees memory occupied by objects that are no longer in use.

      - If an object has no references pointing to it (i.e., nothing is using it), garbage collector removes it from memory.

      - This ensures that unused memory can be reused for new objects.

    # Reference Counting
      -    Every object keeps a reference counter, which tells how many variables (or references) are currently pointing to that object.

      - When a new reference to the object is created, counter increases.

      - When a reference is deleted or goes out of scope, counter decreases.

      - If the counter reaches zero, it means no variable is using the object anymore, so Python automatically deallocates (frees) that memory.

      a = [1, 2, 3]
      b = a

      print(id(a), id(b))   # Same ID → both point to same list

      b.append(4)
      print(a)

      OUTPUT:
      140645192555456 140645192555456
      [1, 2, 3, 4]

      - a and b both refer to same list in memory.
      - Changing b also changes a, because both share same reference.