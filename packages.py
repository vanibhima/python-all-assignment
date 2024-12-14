Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#packages
# Create a directory structure:
# project/
... #     main.py
... #     module/
... #         __init__.py
... #         class1.py
... #         class2.py
... 
... # class1.py
... class Class1:
...     def __init__(self, value):
...         self.value = value
... 
...     def display(self):
...         return f"Class1 value: {self.value}"
... 
... # class2.py
... class Class2:
...     def __init__(self, name):
...         self.name = name
... 
...     def greet(self):
...         return f"Hello, {self.name}!"
... 
... # __init__.py
... # This file is used to indicate that the directory is a Python package.
... # Import the classes to make them accessible when the package is imported.
... from .class1 import Class1
... from .class2 import Class2
... 
... # main.py
... # Import the classes from the module package.
... from module import Class1, Class2
... 
... # Create objects for both classes and call their methods.
... if __name__ == "__main__":
...     # Create an object of Class1
...     obj1 = Class1(42)
...     print(obj1.display())
... 
...     # Create an object of Class2
...     obj2 = Class2("Alice")
...     print(obj2.greet())
