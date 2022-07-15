#! python
def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'idade inválida'

if __name__ == '__main__':
    idade = float(input('Digite a sua idade: '))
    print(f'Você tem {idade:.0f} anos: {faixa_etaria(idade)}')
