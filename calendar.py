Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> man
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    man
NameError: name 'man' is not defined. Did you mean: 'max'?
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import calendar
>>> yy = int(input('Enter year: ')), mm = int(input('Enter month: ')), print(calendar.month(yy,mm))
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> yy= int(input('Enter year: ')
...         2023
...         
SyntaxError: incomplete input
>>> yy= int(input('Enter year: '))
...         
Enter year: 2023
>>> mm= int(input('Enter month: '))
...         
Enter month: 6
>>> print(calendar.month(yy,mm))
...         
     June 2023
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

