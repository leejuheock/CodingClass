import random

a = random.randint(1,100)

v = 0

while True:

    print('up&down 게임입니다 1~100까지의 숫자 중 써보십시오.')

    b = input('')

    v = v+1

    c = int ( b )

    if a == c:
        print('맞았습니다')
        print( '%d번만에 맞히셧습니다' % v )        
        break
    if a > c:
        print('업')

    if a < c:
        print('다운')
        
        
        
    
            

    

