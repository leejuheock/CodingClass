import random

a = random.randint(1,100)

v = 0

while True:

    print('up&down 게임입니다.')

    print('1~100까지 숫자 중 하나를 적어주세요')

    b = input('')

    v = v+1

    c = int ( b )
        
    if a == c:
        print('맞았습니다')
        print( '%d번만에 맞히셧습니다' % v )        
        break
    
    else:
        print('잘못 입력하였습니다.')
    if a > c:
        print('업')

    if a < c:
        print('다운')
        

    
    
            
     
        
    
        
        
    
            

    

