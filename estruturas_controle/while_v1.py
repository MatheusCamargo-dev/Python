#! python
from cores_v1 import cor
from random import randint


random_number = randint(0, 10)
number = -1


while number != random_number:
    number = int(input('Informe um numero de 0 a 10: '))
    if number == random_number:
        print(cor.green+'Aceto mizeravi')
    else:
        print(cor.red+'ERROOOUUU'+cor.none)
