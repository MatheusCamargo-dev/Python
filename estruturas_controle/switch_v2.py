#! python
def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabádo',
    }
    return dias.get(dia, '** Dia invalido**')
def get_dia_ou_fim(dia):
    days = {
        1: 'fim de semana',
        2: 'dia de semana',
        3: 'dia de semana',
        4: 'dia de semana',
        5: 'dia de semana',
        6: 'dia de semana',
        7: 'fim de semana',
    }
    return days.get(dia, '** Dia invalido**')

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)} é um {get_dia_ou_fim(dia)}')

