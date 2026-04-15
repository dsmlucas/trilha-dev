Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 in range(1, 5)
True
>>> 3 in range(1, 5)
True
>>> 3 and 5 in range(1, 6)
True
>>> ((1 and 6) or (5 and 6)) in range(1, 6)
False
>>> ((1 and 2 ) or (2 and 4)) in range(1, 6)
True
>>> ((1 and 2 ) or (2 and 4)) in range(1, 6)
True
>>> (2 or 8) in range (1,6)
True
>>> (2 or 4) in range (1,6)
True
>>> (2 or 12) in range (1,12)
True
>>> (12 or 2) in range (1,12)
False
>>> (8 or 2) in range (1,6)
False

