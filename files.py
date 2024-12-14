Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #files
>>> # Write a program to read text file.
... 
... file1 = open("HW.txt","r")
... data = file1.read()
... print(data)
... print()
... 
... file2 = open("Blank.txt","w")
... str1 = 'Python'
... file2.write(str1)
... print()
... 
... file3 = open("HW.txt","r+")
... print(file3.readline(11))
... print()
... 
