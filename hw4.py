def rep_char(c,n):
  print(c*n)

def draw_line_string(msg):
  msg1='hello {msg}'
  msg2='welcome to seoul'
  nstr=len(msg1)if(len(msg1)>len(msg2)) else len(msg2)
  rep_char('-',nstr+2)
  print(f'hello {msg}, \nwelcome to seoul.')
  rep_char('-',nstr+2)

msg=input('input his/her name:')
draw_line_string(msg)
