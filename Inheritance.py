Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #inheritance
>>> class A():  
...     def display(dp):
...         print("Display Inside class A ")
...  # class A show method    
...     def show(self):
...         print("Show Inside class A")
...     
... # Inherited or Sub class (Note A in bracket) 
... class B (A): 
...     def print(pt):
...         print("Print Inside class B")    
...     # class B show method
...     def show(self):
...         print("Show Inside class B")
...     
... # Inherited or Sub class (Note B in bracket) 
... class C (B): 
...           
...     # class C show method
...     def show(self):
...         print("Show Inside class C ")         
...     
... # Driver code 
... s = A()
... s.display()
... k= B()
... k.print()
... g = C()   
