Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista = [1,2,3]
>>> lista
[1, 2, 3]
>>> lista = + [4,5,6]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lista = + [4,5,6]
TypeError: bad operand type for unary +: 'list'
>>> lista =+ [4,5,6]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lista =+ [4,5,6]
TypeError: bad operand type for unary +: 'list'
>>> lista = lista(("Bom diaaa",))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lista = lista(("Bom diaaa",))
TypeError: 'list' object is not callable
>>> lista = list(("gustavo",))
>>> lista
['gustavo']
>>> lista =+ lista(("dos santos",))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lista =+ lista(("dos santos",))
TypeError: 'list' object is not callable
>>> lista = lista + lista(("dsm",))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lista = lista + lista(("dsm",))
TypeError: 'list' object is not callable
>>> lista
['gustavo']
>>> ["gustavo"]
['gustavo']
