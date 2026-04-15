Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

1 in range (1,5,)
True

0 in range (1,5,)
False

1 not in (1, 2, 3, 4, 5)
False

>>> 6 not in (1, 2, 3, 4, 5)
True
>>> 
>>> 
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = range(1,11)
>>> if 3 in x:
...     print("Contido")
... else:
...     print("Não está contido")
... 
Contido
>>> 
>>> 
>>> if 1 in x:
...     print("Contido")
... else:
...     print("Não está contido") 
...     
Contido
>>> 
>>> 
>>> if 0 in x:
...     print("Contido")
... else:
...     print("Não está contido")
... 
Não está contido
