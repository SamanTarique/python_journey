##### @classmethod
    - @classmethod are those functions which is invoked using class name and recives the class itself as argument. changes done by 
      classmethod will reflect in each instance
    * use case - alternate constructor , modify class attributes , Inheritence: Base class can use alternate constructor feature for themself.

##### @staticmethod
    - staticmethod are those methods which is invoked with class name and dont have niether self nor cls.
    * use case - validation logic , utility function 
  
##### instance methods 
    - instance methods are those methods which are accessable through class instance used for implementing main logics

##### @property
    - property decorator is used to define getter and setter for instance attributes.

##### Duck Typing
    - Having the same name to call/access and serving the same functionality also , but just belongs to the different type( class ) , this behaviour is called duck typing.
    eg. assume google chat and bestpeers portal comes under the same program , just different classes only.They both have many methods but few of them have common name and functionality. here common name and functionality means common attributes and methods name and functionality. So a common method in both the class is submit_report, which updates the status simply.
    so if i do -

    bp = BestPeers()

    gc = GoogleChat()

    def collect_report(employee):
        employee.submit_report()

    collect_report(Manager())
    collect_report(Developer())

    Works for all, because they all can submit_report()
    Duck typing: we only care that employee has submit_report()

    * This is duck typing: don’t care about the actual class, just the behavior (method) it provides.

    ##### Same with the plain variables

        * Adding things together

            - If you add two numbers, you get arithmetic addition.
            - If you add two strings, you get concatenation.
            - If you add two lists, you get list merging.

            * Same + operator, different behavior depending on the variable.
              That’s duck typing — Python doesn’t care about the type, it just looks if the variable supports +

              # Integers
                a = 10
                b = 20
                print(a + b)   # 30 (numeric addition)

                # Strings
                x = "Hello "
                y = "World"
                print(x + y)   # "Hello World" (string concatenation)

                # Lists
                list1 = [1, 2]
                list2 = [3, 4]
                print(list1 + list2)   # [1, 2, 3, 4] (list merging)

            ##### Why this is duck typing?

                Because the same operator + works differently depending on the type of variable:

                For numbers → adds values

                For strings → concatenates text

                For lists → extends sequences

                Python doesn’t check type explicitly. It just says:
                “Does this variable support __add__? If yes, run it.”

##### Operator Overloading
    - Python achieves operator overloading through special methods (also known as "magic methods" or "dunder methods") that begin 
    and end with double underscores, such as __add__ for the + operator, __sub__ for -, __mul__ for *, and so on. When an operator 
    is used with objects of a custom class, Python automatically calls the corresponding special method defined within that class.

    
