#! python
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('É necessário informar o raio do circulo')
    print(f'Sintaxe: {sys.argv [0][2:]} <raio>''')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    if not sys.argv[1].isnumeric():
        help()
        print('Retorne um valor númerico')
        sys.exit(2)

raio = sys.argv[1]
area = circulo(raio)
print(f' A área do circulo é {area}')
