Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Write two methods with the same name but different number of parameters of same type and call the methods
>>> 
>>> class Demo:
...     def method(self, a, b=None):  # Default argument for the second parameter
...         if b is None:
...             print(f"Method with one parameter: a = {a}")
...         else:
...             print(f"Method with two parameters: a = {a}, b = {b}")
... 
... # Create an object of the class
... obj = Demo()
... 
... # Call the method with one parameter
... obj.method(10)
... 
... # Call the method with two parameters
... obj.method(10, 20)
... class Demo:
...     def method(self, *args):
...         if len(args) == 1:
...             print(f"Method with one parameter: a = {args[0]}")
...         elif len(args) == 2:
...             print(f"Method with two parameters: a = {args[0]}, b = {args[1]}")
...         else:
...             print("Unsupported number of parameters!")
... 
... # Create an object of the class
... obj = Demo()
... 
... # Call the method with one parameter
... obj.method(10)
... 
... # Call the method with two parameters
... obj.method(10, 20)
