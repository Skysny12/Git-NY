class Point:
  def __init__(self,x=0,y=0):
    self.__x=x
    self.__y=y
  def show(self):
    print(f'({self.__x},{self.__y})')
  def set(self,x,y):
    self.__x=x
    self.__y=y
  def get(self):
    return (self.__x,self.__y)

class Rectangle:
  def __init__(self,x1,y1,x2,y2):
    self.__x1=x1
    self.__x2=x2
    self.__y1=y1
    self.__y2=y2
    (x1<x2,y1<y2)
  def show(self):
    print(f'좌측 상단 꼭지점이 ({self.__x1},{self.__y1})이고 우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다')
  def getHeight(self):
    h=self.__y1 - self.__y2
    return h
  def getWidth(self):
    w=self.__x2 - self.__x1
    return w
  def getArea(self):
    height=abs(self.getHeight())
    width=abs(self.getWidth())
    area=height*width
    return area
  def getPerimeter(self):
    height=self.getHeight()
    width=self.getWidth()
    perimeter=2*height+2*width
    return perimeter

r1=Rectangle(5,5,20,10)
a=r1.getArea()
p=r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a},둘레는 {p}')
