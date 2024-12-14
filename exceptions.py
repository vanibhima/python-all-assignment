Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Exceptions
... a = [1, 2, 3]
... try:
...     print ("Second element = ",a[1])
...  
...     # Throws error since there are only 3 elements in array
...     print ("Fourth element = ",a[3])
...     
... except:
...     print ("An error occurred")
... 
... print()
... 
... b = [3,2,1]
... try:
...     a == b
... except:
...     print("They are not equal")
... else:
...     print("Both Equal") 
... 
... print()
... 
... try:
...     k = 5/0
...     print(k)
... except ZeroDivisionError:
...     print("Can't divide by zero")
... finally:
