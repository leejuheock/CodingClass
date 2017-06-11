import random

a = random.randint(1,100)

l = []

def up():
    print('l')
    print('l    )  ')
    print('l     )  ')
    print('       ) ')
    print('l*** ****)')
    print('l ********* )')
    print(' **********   )')
    print('ㅡㅡㅡㅡㅡㅡㅡㅡ')

def down():

    print('-----------')
    print(' *********!')
    print(' *********')
    print('**** ****!')
    print('l  _!')
    print('_')

while True:

    print('up&down 게임입니다 1~100까지의 숫자 중 써보십시오.')

    b = input('') 

    try:
        c = int ( b )
    except:
        print('숫자로 입력하세요.')
        continue
   
    if 100 >= c > 0:
        if c in l:
            print('이미 입력한 숫자입니다.')
        else:
            l.append(c)
        if a > c:
            up()
        if a < c:
            down()
        if a == c:
            print('맞았습니다.')
            print('%d번만에 맞히셧습니다' % len(l
                                       ))
            break
    else:
        print('오차범위 입니다.1에서 100 중 숫자를 써주세요.')
        

    

