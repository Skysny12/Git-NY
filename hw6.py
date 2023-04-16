Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for j in range(1,10):
...   for i in range(2,6):
...       print(f'{i} x{j:2d} = {j*i:2d}',end='\t')
...   print()
... 
... print()    
... 
... for j in range(1,10):
...   for i in range(6,10):
...       print(f'{i} x{j:2d} = {j*i:2d}',end='\t')
