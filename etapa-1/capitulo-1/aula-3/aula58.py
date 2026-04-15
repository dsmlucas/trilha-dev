Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "Teste"
len(s)
5

s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
len(s)
45
len("")
0
len("1")
1

print(s)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


S = "ABCDEFGHIJK"
len(s)
45

s = "ABCDEFGHIKL"
len(s)
11

print(s)
ABCDEFGHIKL
s[2]
'C'
s[1]
'B'
s[0:]
'ABCDEFGHIKL'
s[0:2]
'AB'

s.split(" ")
['ABCDEFGHIKL']
>>> 
>>> s = "Olá Gustavo"
>>> print(s)
Olá Gustavo
>>> s.split(" ")
['Olá', 'Gustavo']
>>> lista[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    lista[0]
NameError: name 'lista' is not defined. Did you mean: 'list'?
>>> lista[0]+" "+lista[2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lista[0]+" "+lista[2]
NameError: name 'lista' is not defined. Did you mean: 'list'?
>>> lista
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lista
NameError: name 'lista' is not defined. Did you mean: 'list'?
>>> print
<built-in function print>
>>> print(s)
Olá Gustavo
>>> s
'Olá Gustavo'
>>> s.split(" ")
['Olá', 'Gustavo']
>>> lista = s.split(" ")
>>> lista
['Olá', 'Gustavo']
>>> lista[0]+" "+lista[1]
'Olá Gustavo'

>>> s = "Teste"
    print(s)
Teste

>>>id(s)
1777195377776
>>>\id(s.replace("Lista", ""))
1777195377776