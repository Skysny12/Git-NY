Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
... 
... def input_scores():
...   num=[]
...   i=0
...   while True:
...     n=int(input(f'#{i+1}?'))
...     num.append(n)
...     i+=1
...     if n<0:
...       break
...   return num
... 
... def get_average(s):
...     total = sum(s)
...     if len(s) > 0:
...         return total / len(s)
...     else:
...         return 0
...    
... 
... def show_scores(s):
...   for n in s:
...     print(n, end=' ')
...   print()
... 
... def save_data(num,filepath):
...   with open(filepath,'w')as file:
...     for item in num:
...       file.write(f'{item}\n')
...     file.write(f'{avg}\n')
... 
... 
... def load_data(filepath):
...   with open(filepath,'r')as file:
...     lines=file.readlines()
...     num = [int(line.strip()) for line in lines]
  return num
    
    
filepath='score.bin'
if os.path.exists(filepath):
  print('[파일 읽기]')
  print('[점수 출력]')
  num=load_data(filepath)
  show_scores(num)
 


else:
  print('{점수 입력}')
  scores=input_scores()
  print('\n[점수출력]')
  print('개인점수:',end='')
  show_scores(scores)
  avg=get_average(scores)
  print(f'평균:{avg:.1f}')
