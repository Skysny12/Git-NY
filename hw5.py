def read_single_digit(th):
  if th==1:
    return('일')
  elif th==2:
    return('이')
  elif th==3:
    return('삼')
  elif th==4:
    return('사')
  elif th==5:
    return('오')
  elif th==6:
    return('육')
  elif th==7:
    return('칠')
  elif th==8:
    return('팔')
  elif th==9:
    return('구')
  else:
    return('영')

def read_number(num):
  n=num
  n100=n//100
  n%=100
  n10=n//10
  n%=10
  n1=n//1
  n%=1
  a=read_single_digit(n100)
  b=read_single_digit(n10)
  c=read_single_digit(n1)
  print(f'{a} {b} {c}')

n=int(input('세자리수 입력'))
read_number(n)
