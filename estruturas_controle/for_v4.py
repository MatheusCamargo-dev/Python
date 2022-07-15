#! python
from random import randint
def random():
    return randint(1, 6)

for x in range (1,7):
    if x % 2 == 1:
        continue
    elif x == random:
        print(f'Você acertou o numero {random}')
        break
else: print('Não acertou o numero')

    
