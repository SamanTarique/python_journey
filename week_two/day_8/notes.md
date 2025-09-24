# OOP
> As the name suggests, Object-Oriented Programming or OOPs refers to languages that use objects in programming. Object-oriented 
programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming. The main aim of OOP 
is to bind together the data and the functions that operate on them so that no other part of the code can access this data except 
that function.

>>**Class:**
A class is a user-defined data type. It consists of data members and member functions, which can be accessed and used by creating 
an instance of that class. It represents the set of properties or methods that are common to all objects of one type. A class is 
like a blueprint for an object.  

For Example: Consider the Class of Cars. There may be many cars with different names and brands but all of them will share some 
common properties like all of them will have 4 wheels, Speed Limit, Mileage range, etc. So here, Car is the class, and wheels, 
speed limits, mileage are their properties.

>> **Object:**
It is a basic unit of Object-Oriented Programming and represents the real-life entities. An Object is an instance of a Class. When 
a class is defined, no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated. An object 
has an identity, state, and behavior. Each object contains data and code to manipulate the data. Objects can interact without 
having to know details of each other’s data or code, it is sufficient to know the type of message accepted and type of response 
returned by the objects. 

For example “Dog” is a real-life Object, which has some characteristics like color, Breed, Bark, Sleep, and Eats.

>> **Data Abstraction:**
Data abstraction is one of the most essential and important features of object-oriented programming. Data abstraction refers to 
providing only essential information about the data to the outside world, hiding the background details or implementation. 
Consider a real-life example of a man driving a car. The man only knows that pressing the accelerators will increase the speed of 
the car or applying brakes will stop the car, but he does not know about how on pressing the accelerator the speed is increasing, 
he does not know about the inner mechanism of the car or the implementation of the accelerator, brakes, etc in the car. This is 
what abstraction is.

>> **Encapsulation:**
Encapsulation is defined as the wrapping up of data under a single unit. It is the mechanism that binds together code and the data
it manipulates. In Encapsulation, the variables or data of a class are hidden from any other class and can be accessed only
through any member function of their class in which they are declared. As in encapsulation, the data in a class is hidden from 
other classes, so it is also known as data-hiding.

Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section, etc. The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section. He will first have to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”.

>> **Inheritance:**
Inheritance is an important pillar of OOP(Object-Oriented Programming). The capability of a class to derive properties and
characteristics from another class is called Inheritance. When we write a class, we inherit properties from other classes. So when 
we create a class, we do not need to write all the properties and functions again and again, as these can be inherited from 
another class that possesses it. Inheritance allows the user to reuse the code whenever possible and reduce its redundancy.

![This is an alt text.](https://media.geeksforgeeks.org/wp-content/uploads/20200911171738/InheritanceinObjectOrientedProgramming.png "This is a sample image.")

>> **Polymorphism:**
The word polymorphism means having many forms. In simple words, we can define polymorphism as the ability of a message to be
displayed in more than one form. For example, A person at the same time can have different characteristics. Like a man at the same
time is a father, a husband, an employee. So the same person posses different behavior in different situations. This is called 
polymorphism.
![This is an alt text.](https://media.geeksforgeeks.org/wp-content/uploads/20200911171857/PolymorphisminObjectOrientedProgramming.png "This is a sample image.")

#### Why do we need object-oriented programming
    - To make the development and maintenance of projects more effortless. 
    - To provide the feature of data hiding that is good for security concerns.  
    - We can solve real-world problems if we are using object-oriented programming. 
    - It ensures code reusability. 
    - It lets us write generic code: which will work with a range of data, so we don't have to write basic stuff over and over again.

### Class
In object-oriented programming (OOP), a class is a blueprint or template for creating objects, defining both the data (attributes) 
and behaviors (methods) that objects of that type will have. It's a user-defined type that bundles together characteristics and 
functions, providing a structure for creating multiple, distinct objects that share common properties and actions.

**Some points on Python class:**  

- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

**A class is a logical construct; it does not occupy memory by itself until an object (an instance of the class) is created from 
it.** 


### Object
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

### Self Parameter
Self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the 
object.

Example: In this example, we create a Dog class with both class and instance attributes, then demonstrate how to access them using 
the self parameter.

### __init__ Method
__init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of 
the class.

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.name)
```

Example: In this example, we create a Dog class and use __init__ method to set the name and age of each dog when creating an 
object.

#### Class and Instance Variables
In Python, variables defined in a class can be either class variables or instance variables, and understanding the distinction between them is crucial for object-oriented programming.

**Class Variables:**

These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

**Instance Variables:**

Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

**Example: In this example, we create a Dog class to show difference between class variables and instance variables. We also demonstrate how modifying them affects objects differently.**

```
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)
```