Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista = [1,2,3,4,5]
>>> lista
[1, 2, 3, 4, 5]
>>> lista = lista + [6]
>>> lista
[1, 2, 3, 4, 5, 6]
>>> lista = [1]
>>> lista = lista + [2]
>>> lista
[1, 2]
>>> lista = [1,2,3,4,5,6,7,8,9]
>>> lista = lista + [10]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lista = [1,2,3,4,5]
>>> lista = lista + [,6,7,8,9,10]
SyntaxError: invalid syntax
>>> lista = lista + [6,7,8,9,10]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del(lista[-1])
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista+= 10*[0]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 10*"-"
'----------'
>>> 10*"@"
'@@@@@@@@@@'
>>> '@@@@@@@@@@'
'@@@@@@@@@@'
>>> 100*"0!
SyntaxError: unterminated string literal (detected at line 1)
100*"0"
'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
del(lista[-1])
lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
