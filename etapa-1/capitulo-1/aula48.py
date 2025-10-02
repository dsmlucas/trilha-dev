Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lista = "Bem vindo"
lista [10]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lista [10]
IndexError: string index out of range
>>> lista[a]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lista[a]
NameError: name 'a' is not defined
>>> lista[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lista[10]
IndexError: string index out of range
>>> lista = "Bem vindo ao curso de PYTHON"
>>> lista[10]
'a'
>>> lista[11]
'o'
>>> lista[1]
'e'
>>> lista = "Gustavo dsm"
>>> lista[1]
'u'
>>> lista[0]
'G'
>>> lista[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lista[1,2,3,4]
TypeError: string indices must be integers, not 'tuple'
>>> lista[7]
' '
>>> lista[8]
'd'
>>> lista[1:10]
'ustavo ds'
>>> lista[0:11]
'Gustavo dsm'
