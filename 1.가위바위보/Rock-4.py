
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

def display(x):
    if x == 1:
        gawi()

    if x == 2:
        bawi()

    if x == 3:
        bo()
        
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
    print ('제가 낸 것')
    display(a)    
    
    print('당신이 낸 것 ')
    display(d)
        
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
        


    
        
        

