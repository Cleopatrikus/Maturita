import os
from random import randint

if os.path.exists('s.txt'):
    os.remove('s.txt')
    
with open('s.txt', 'w') as s:
    body = 0
    priklady = []
    text = ''
    
    for i in range(10):
        x1, x2 = randint(0, 9), randint(0, 9)
        text = f'{x1} * {x2} ='
        while text in priklady:
            x1, x2 = randint(0, 9), randint(0, 9)
            text = f'{x1} * {x2} ='
        #text = f'{x1} * {x2} = {x1 * x2}'

        print(text, end = ' ')
        answer = int(input())
        s.write(text + '\n')
        
        if answer == x1 * x2:
            body += 1
        priklady.append(text)
        
    print('Pocet bodov je {}'.format(body))
        
    
    
