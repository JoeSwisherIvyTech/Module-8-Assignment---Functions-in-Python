Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def greater_than(x, y):
...     if x > y:
...         return True
...     else:
...         return False
... 
...     
>>> def output_result(result):
...     print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
...     return
... 
>>> a = 2
>>> b = 3
>>> 
>>> result = greater_than(a, b)
>>> output_result(result)
The statement 2 is greater than 3 is False
>>> a = 10
>>> b = 6
>>> result = greater_than(a, b)
>>> output_result(result)
The statement 10 is greater than 6 is True
