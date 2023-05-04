d={}
while True:
  item=input('상품명?')
  if item=='':
    break
  lens=input('수량은?')
  d[item]=lens
  print(f'장바구니에 {item} {lens}개가 담겼습니다.','\n')
  

print('>>>장바구니 보기:',d,'\n')
print('[검색]')
r=input('장바구니에서 확인하고자 하는 상품은?')
res=d.get(r)
print(r,'은(는)',res,'개 담겨있습니다')
