def get_radius(prompt):
    r=int(input(prompt))
    return r
def get_circle(r):
    area=r*r*3.14
    print('반지름이',r,'인','원의 넓이는',area)
r=get_radius('원의 반지름은?')
get_circle(r)
