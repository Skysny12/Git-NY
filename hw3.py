def get_fixed_price(A):
  amount=A/((100-Z)/100)
  print('A상품의 정가는',amount,'원')

def get_fixed_price(B):
  am=B/((100-Z)/100)
  print('B상품의 정가는',am,'원')




Z=int(input('할인율은?'))
A=int(input('A상품의 할인된 가격은?'))
B=int(input('B상품의 할인된 가격은?'))
get_fixed_price(A)
get_fixed_price(B)
