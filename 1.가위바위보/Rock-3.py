
import random

print('가위바위보 게임입니다')

while True:
    a = random.randint(1, 3)
    print('')
    print('1=가위 2=바위 3=보')
    print('무엇을 내실건가요?')
    c = input('')
    d = int(c)
    if d == 0:
        print('게임이 끝납니다')
        break
    
    if a == d:
        print('비겻다')
    if (a == 1 and d == 2) or (a == 2 and d == 3) or (a == 3 and d == 1 ):
        print('니가 이겻다')
    if (a == 2 and d == 1) or (a == 3 and d == 2) or (a == 1 and d == 3):
        print('내가 이겻다')

    if a == 2:
        x = '바위'
    if a == 3:
        x = '보'
    if d == 1:
        y = '가위'
    if d == 2:
        y = '바위'
    if d == 3:
        y = '보'
    if d < 4 and d > 0:
        print('제가 낸 것 %s' % x )
        print('당신이 낸 것 %s' % y )
    else:
        print('잘못 입력하셧습니다.')
        


    
        
        

