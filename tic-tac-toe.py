#TIC TAC TOE
import time
import random

print('Welcome')
print('to')
#time.sleep(1)
print('TIC')
#time.sleep(2)
print('TAC')
#time.sleep(2)
print('TOEEEEEEE')


posit=['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R']
game='running'
player=1



pos={'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printboard(pos):
    
    print(pos['top-L'],'|',pos['top-M'],'|',pos['top-R'],'|')
    print('-----------')
    print(pos['mid-L'],'|',pos['mid-M'],'|',pos['mid-R'],'|')
    print('-----------')
    print(pos['low-L'],'|',pos['low-M'],'|',pos['low-R'],'|')
    print('-----------')


def gameover():
    global game
    if pos['top-L']==pos['mid-M']==pos['low-R'] and pos['top-L']!=' ':
        game='won'
    elif pos['top-R']==pos['mid-M']==pos['low-L'] and pos['top-R']!=' ':
        game='won'
    elif pos['top-L']==pos['top-M']==pos['top-R'] and pos['top-L']!=' ':
        game='won'
    elif pos['top-L']==pos['mid-L']==pos['low-L'] and pos['top-L']!=' ':
        game='won'
    elif pos['low-L']==pos['low-M']==pos['low-R'] and pos['low-L']!=' ':
        game='won'
    elif pos['low-R']==pos['mid-R']==pos['top-R'] and pos['low-R']!=' ':
        game='won'
    elif pos['top-L']!=' ' and pos['top-M']!=' ' and pos['top-R']!=' ' and pos['mid-L']!=' ' and pos['mid-M']!=' ' and pos['mid-R']!=' ' and pos['low-L']!=' ' and pos['low-M']!=' ' and pos['low-R']!=' ':
        game='draw'
    else:
        game='running'

def check(x):
    if pos[x]==' ':
        return True
    else:
        return False
        

print('X or O')
user=input()
if user=='X':
    opponent='O'
else:
    opponent='X'
    
    
while game=='running':
    printboard(pos)
    
    if player%2!=0:
        print('Choose a move user (top-L,M,R mid-L,M,R low-L,M,R)')
        choice=input()
        if check(choice):
            pos[choice]=user
            player+=1
          
    if player%2==0:
        computer=random.choice(posit)
        if check(computer):
            pos[computer]=opponent
            player+=1
    gameover()
            
printboard(pos)
if game=='draw':
    print('DRAW')
elif game=='won':
    player-=1
    if player%2!=0:
        print('You won')
    else:
        print('Computer won')
        
    
        


    
