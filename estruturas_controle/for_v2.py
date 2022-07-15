#! python
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end='-')
print ('FIM')


aprovados = ['Matheus', 'Gabriel', 'Emerson', 'Richard']
for nome in aprovados:
    print (nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo','Segunda','Terça',
                  'Quarta','Quinta','Sexta','Sabádo')

for dia in dias_semana:
    print(f'hoje é {dia}')