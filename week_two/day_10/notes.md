# @staticmethod
    - it is method defined inside a class , but not associated with the class instance. its related to the class and called by class name.
    - Unlike instance methods (which receive self) or class methods (which receive cls), static methods do not receive an implicit first argument representing either the instance or the class.

    # use cases
        * utility function ( mini logic blocks with specific purpose)
            eg: 1.arthematic calculations between class attributes or passed variable
                2.validation logic
                3 factory methods ? kya hota hai

# @classmethod
    - it is a type of method bound to the class and not the instance of the class. It is defined using the @classmethod decorator and receives the class itself, conventionally named cls, as its first argument. This means a class method can access and modify class-level state that applies across all instances of the class. 
    - Here the cls is the class itself so it used as an alternative constructor of the class

    # use case
        - Alternative constructors
        - Modifying or accessing class state
        - Inheritance and polymorphism: When a class method is used in a parent class, a subclass that inherits it will receive cls as a reference to the subclass itself, not the parent. This makes class methods especially useful for factory methods in an inheritance hierarchy, as they will automatically create an instance of the correct derived class.

# @property
    - The @property decorator in Python is a built-in feature that provides a Pythonic way to manage class attributes. It simplifies the creation of methods that can be accessed like attributes, allowing you to implement custom logic for getting, setting, and deleting an attribute's value.

    # use case
        - Data validation(while setting value)
        
        - Calculated Attributes: You can create attributes that are computed dynamically. For example, a Circle class can have a diameter property that calculates its value from the radius each time it is accessed.
        
        - Improved Readibility ( obj.get_name instead of obj.get_name())
        
        - Read-Only Attributes: By defining only a getter method with @property and no setter, you can create a read-only attribute that cannot be modified from outside the class.
        
        - Backward Compatibility: If you start with a simple public attribute and later need to add validation or other logic, you can convert it into a property without changing the syntax used by external code. This prevents breaking a class's public API.
