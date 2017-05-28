
import random

print('가위바위보 게임입니다')

l = ['가위','바위','보']

def gawi():
    print('    *    *')
    print('    *   *')
    print('    *  *')
    print('    * *')
    print('    ***')
    print('   ******')
    print(' ********')
    print('   *****')
    print('    ***')

def bawi():
    print('')
    print('')
    print('')
    print('')
    print('    ***')
    print('   ******')
    print(' ********')
    print('   *****')
    print('    ***')

def bo():
    print('    *  *  ')
    print('    *  *  *')
    print('    *  *  * *')
    print('    *  * * *')
    print('*   * * * *')
    print('**  ******')
    print(' ********')
    print('   *****')
    print('    ***')

while True:
    a = random.randint(1, 3)
    print('')
    print('1=가위 2=바위 3=보')
    print('무엇을 내실건가요?')
    
    c = input('')
    try:
        d = int(c)
    except:
        print('숫자(가위 바위 보)로 입력해주세요.')
        continue
    if d == 0:
        print('게임이 끝납니다')
        break

    if a == 1:
        print(gawi()'제가 낸 것')
         
    if a == 2:
        print(bawi() '제가 낸 것')
            
    if a == 3:
        print(bo()'제가 낸 것')

    if d == 1:
        print (gawi()'당신이 낸 것 ')

    if d == 2:
        print (bawi()'당신이 낸 것')
    
    if d == 3:
        print (bo() '당신이 낸 것')
        
    if a == d:
        print('비겻다')
    if (a == 1 and d == 2) or (a == 2 and d == 3) or (a == 3 and d == 1 ):
        print('니가 이겻다')
    if (a == 2 and d == 1) or (a == 3 and d == 2) or (a == 1 and d == 3):
        print('내가 이겻다')

    if 4 > d > 0:
        print('제가 낸 것 %s' % l[a-1] )
        print('당신이 낸 것 %s' % l[d-1] )
    else:
        print('잘못 입력하셧습니다.')
        


    
        
        

