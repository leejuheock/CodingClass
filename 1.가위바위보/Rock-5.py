
import random


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


a = random.randint(1, 3)
if a == 1:
    gawi()
if a == 2:
    bawi()
if a == 3:
    bo()


