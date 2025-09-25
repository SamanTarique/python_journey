##### Pytest
    - pytest is a popular testing framework for Python that simplifies the process of writing and executing tests. It is mainly 
    used to write API test cases. It helps you write better programs. In the present days of REST services, Pytest is mainly 
    used for API testing even though we can use Pytest to write simple to complex test cases, i.e., we can write codes to test 
    API, UI, database, etc.

    * At its core, pytest does three things:

        Discovery – It finds your test files and functions using naming conventions.

        Execution – It runs the test functions.

        Reporting – It shows a detailed summary of passed, failed, and skipped tests.

    * Test discovery rules

        Test files: test_*.py or *_test.py

        Test functions: Must start with test_

        Test classes: Must start with Test (no __init__ allowed), methods must start with test_

    * Assertions
        - Assertion is the boolean expression that checks if the statement is True or False. If the statement is true then it 
        does nothing and continues the execution, but if the statement is False then it stops the execution of the program and 
        throws an error.
        - Pytest lets you write plain Python asserts

        def add(a, b):
            return a + b

        def test_add():
            assert add(2, 3) == 5
            assert add(-1, 1) == 0
    
    * Fixtures
        - A Fixture is a piece of code that runs and returns output before the execution of each test.
        
        - Fixtures are a powerful feature that allows you to set up and tear down resources needed for your tests. They help in 
          creating reusable and maintainable test code by providing a way to define and manage the setup and teardown logic
            
    * Parameterization
        - Run a test with multiple inputs
        - Saves you from writing repetitive tests
        - Great for edge-case testing
