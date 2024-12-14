Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Define the local and Global variables with the same name and print both variables and understand the scope of the variables
>>> 
>>> #global variable
>>> x=10
>>> def fun():
... #local variable
...     x=20
...     print("local varible x:",x) #this will access the local 'x'
... #print the global varible
...     print("global variable x:",x)
... 
...     
>>> #call function
...     
>>> fun()
local varible x: 20
global variable x: 20
>>> print("global varible x after function call:",x)
global varible x after function call: 10
