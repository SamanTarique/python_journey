##### module
    - A module is a file containing Python code, typically saved with a .py extension. It serves as a way to organize and logically group related code, such as functions, classes, and variables.

    * Code Organization:
    Modules allow you to break down large programs into smaller, more manageable, and reusable units. This improves code 
    readability and maintainability.

    * Reusability:
    Code defined within a module can be easily reused across different Python scripts or other modules by importing it. This 
    eliminates the need to rewrite the same code multiple times.

##### package
    - A package is essentially a directory (folder) that contains one or more Python modules (individual .py files) and 
    potentially sub-packages (nested directories that are themselves packages)

    - __init__.py file:
    Every directory intended to be a Python package must contain a special file named __init__.py. This file can be empty, but its 
    presence signifies to Python that the directory should be treated as a package. When a package is imported, the code within 
    its __init__.py file is executed, allowing for package-level initialization or the definition of package-level variables, 
    functions, or classes.

    - Modules:
    Within a package, individual Python files (e.g., module1.py, module2.py) are considered modules. These modules contain the 
    actual Python code, including functions, classes, and variables.

    - Sub-packages:
    Packages can contain other packages as sub-packages, creating a nested hierarchy. Each sub-package also requires its own 
    __init__.py file.