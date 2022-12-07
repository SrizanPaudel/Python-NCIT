Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> add=lambda c:c*10
>>> add(10)
100
>>> add(5)
50
>>> add=lambda a,b: a*b
>>> add(10,4)
40
>>> [x+2 for x in range(1,20)]
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
>>> [x+2 for x in range(1,20,2)]
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
>>> [x+2 for x in range(1,20)if x>5]
[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
>>> {x:x+2 for x in range(10)}
{0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}
