Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #static
>>> # Define a static variable and access that through a class.
... 
... class Python:
... # Access through class    
...  staticVariable = 9 
... print(Python.staticVariable)
... 
... #Change within an class
... Python.staticVariable = 12
... print(Python.staticVariable) # Gives 12
... 
... #Access through an instance
... instance = Python()
... print(instance.staticVariable) # Gives 12
... 
... #Change within an instance
... instance.staticVariable = 15
... print(instance.staticVariable) # Gives 15
