Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def buy(a):
...   b=input('상품명?')
...   c=input('수량은?')
...   if b=='' or c=='':
...     return False
...   print(f'장바구니에 {b} {c}개가 담겼습니다.')
...   a[b]=c
...   return True
... 
...   
... 
... def show(a):
...   print(f'>>>장바구니 보기 :',a)
... 
... def find(a):
...   print('[검색]')
...   z=input('장바구니에서 확인하고자 하는 상품은?')
...   if z in a:
...     print(f'{z}는 {a[z]}개 담겨있습니다')
...   else:
...     print(f'장바구니에 {z}은(는) 없습니다')
... 
... shopping_bag={}
... while True:
...   if buy(shopping_bag)==False:
...     break
... show(shopping_bag)
