# Identity operators

    - identity operators are used to compare the memory locations (identities) of two objects — that is, whether they refer to the same object in memory, not just whether their values are equal.

    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print(a is b)      # True  → both point to the same list object
    print(a is c)      # False → different objects in memory
    print(a == c)      # True  → values are equal

    x = 10
    y = 10

    print(x is y)  # True (small integers are cached by Python)

    ✅ Python internally caches some immutable objects (like small integers and short strings), so they may share the same memory.

    is → compares object identity (same memory)

    == → compares values (data equality)

# Implicit type conversion

    - Performed automatically by Python, without any action from the programmer.It happens when Python upgrades one data type to another to
    prevent data loss.

# Explicit type conversion

    - You do it manually, using built-in functions like:

    int()
    float()
    str()
    list()
    tuple()
    set()
    bool()
