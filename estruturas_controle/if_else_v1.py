#! python

from cores_v1 import cor


def nota_conceito(valor):
    nota = float(valor)
    if nota >= 0 and nota <= 10:
        if nota <= 10 and nota > 9:
            return 'A'
        elif nota >= 8.1:
            return 'A-'
        elif nota >= 7.1:
            return 'B'
        elif nota >= 6.1:
            return 'B-'
        elif nota >= 5.1:
            return 'C'
        elif nota >= 4.1:
            return 'C-'
        elif nota >= 3.1:
            return 'D'
        elif nota >= 2.1:
            return 'D-'
        elif nota >= 1.1:
            return 'E'
        elif nota >= 0:
            return'E-'
    else:
        print(cor.red+'NOTA INVÁLIDA'+cor.none)


if __name__ == '__main__':
    nota_informada = input('Digite a nota do aluno: ')
    conceito = nota_conceito(nota_informada)
    print(f'a sua nota é {cor.green}{conceito}{cor.none}.')
