Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t= tuple("abc")
>>> t
('a', 'b', 'c')
>>> a= tuple("123")
>>> a
('1', '2', '3')
>>> class ( (1,2,3,4,5,6,7,8,9) )
SyntaxError: invalid syntax
>>> type ( (1,2,3,4,5,6,7,8,9) )
<class 'tuple'>
>>> a = (1,2,3)
>>> a
(1, 2, 3)
>>> 
>>> x = "abc", 1, True
>>> x
('abc', 1, True)
>>> x= "Gustavo", 16,
>>> x = "Gustavo", 16, True
>>> x
('Gustavo', 16, True)
>>> x = "Gustavo", 16
>>> x
('Gustavo', 16)
>>> type(x)
<class 'tuple'>
>>> type(y)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(y)
NameError: name 'y' is not defined
>>> y = "aaa", 16, True
>>> y
('aaa', 16, True)
>>> type(y)
<class 'tuple'>
>>> y
('aaa', 16, True)

>>>cliente = ('Gustavo', 'bairro Humaíta', 'cidade Tubarão')
>>>clientes = []
>>>clientes.append(cliente)
>>>print(clientes)
[('Gustavo', 'bairro Humaíta', 'cidade Tubarão')]
