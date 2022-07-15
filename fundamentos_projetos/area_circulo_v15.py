#! python
from math import pi
import sys
from cores_v1 import cor


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print(f'É necessário informar o raio do {cor.red}circulo{cor.none}')
    print(f'Sintaxe: {sys.argv [0][2:]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    if not sys.argv[1].isnumeric():
        help()
        print(cor.red+'Retorne um valor númerico'+cor.none)
        sys.exit(2)

raio = sys.argv[1]
area = circulo(raio)
print(f' A área do circulo é {cor.cyan}{area:.2f}{cor.none}')
