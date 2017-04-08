
import random
a=random.randint(1, 3)
c=input('?')
d=int(c)
if a==d:
    print('비겻다')
if (a==1 and d==2)or(a==2 and d==3)or(a==3 and d==1):
    print('니가 이겻다')
if (a==2 and d==1)or(a==3 and d==2)or(a==1 and d==3):
    print('내가 이겻다')

    
    
